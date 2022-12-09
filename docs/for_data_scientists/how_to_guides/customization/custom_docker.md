# Run RIME on Managed Docker Images

There may be circumstances when you need to run RIME with a model which requires additional dependencies that are not specified in the provided base testing engine image.

This guide will cover how to run RIME with a custom Docker image when you need a particular version of a library or any additional dependencies to run your model.

This guide assumes that your administrator has enabled the [Managed Images](/for_admins/installation_guide/enterprise/installation/values.md) feature in your RIME deployment.
This feature allows you to create Docker images directly from the SDK without needing to manually write Dockerfiles.
You can also use this feature to query for existing Managed Images so that you can easily find images with the requirements you need and use the same images across teams.
Finally, when you upgrade your version of RIME, your old managed images will still be usable because the RIME backend will upgrade them to be compatible with the latest version.

*Note: The following assumes you have instantiated Client, and that you are familiar with running RIME with the RIME SDK. To learn more about the RIME SDK, please refer to the [SDK Reference](/for_data_scientists/reference/python-sdk.md) for more information.*

### Building a Managed Docker Image

The Managed Images feature allows you to build custom Docker images directly from the SDK.
You only need to specify the name of the image to use as an alias, the list of additional package requirements to be installed, and, optionally, the type of base image you want (all, images, nlp, or tabular).
If not given, the image type will default to use the most general 'all' image type.

Say you have a Tabular model that requires `xgboost` at version `1.0.2` and `tensorflow` at a flexible version.
You can call this image `"xgboost102_tensorflow"` as an alias to remember it later.

{{ sdk_client_setup }}

Next, you may use the helper method `Client.pip_requirement(library_name: str, version_spec: Optional[str])` to construct
a list of pip requirements for your image.
The first argument is the name of the library (e.g. `"tensorflow"` or `"xgboost"`) and the second argument is a valid pip
[version specifier](https://www.python.org/dev/peps/pep-0440/#version-specifiers) (e.g. `">=0.1.2"` or `"==1.0.2"`).
Omitting the version specifier is equivalent to not fixing the version.

```python
requirements = [
  # Fix the version of `xgboost` to `1.0.2`.
  rime_client.pip_requirement("xgboost", "==1.0.2"),
  # We do not care about the installed version of `tensorflow`.
  rime_client.pip_requirement("tensorflow")
]
```

To start the job that will build your custom image, use `rime_client.create_managed_image(name: str, requirements: List[ManagedImage.PipRequirement], image_type: Optional[ImageType])`.
The return value will be a Python class that you can use to track the status of the image building job.

Finally, you can specify the type of RIME managed image you want to use as a base for your custom image.
There are 4 types of base images you can use depending on what sort of models you want to stress test:
  * `ImageType.ALL`: includes all dependencies required to run RIME for any of our stress tests.
  * `ImageType.IMAGES`: includes only the dependencies required to run RIME for image stress tests.
  * `ImageType.NLP`: includes only the dependencies required to run RIME for nlp stress tests.
  * `ImageType.TABULAR`: includes only the dependencies required to run RIME for tabular stress tests.
By building your custom image for a particular type of stress test, you reduce your image's dependencies and total size.

```python
# Start a new image building job
builder_job = rime_client.create_managed_image("xgboost102_tensorflow", requirements, image_type=ImageType.TABULAR)

# Wait until the job has finished and print out status information.
# Once this prints out the `READY` status, your image is available for use in stress tests.
builder_job.get_status(verbose=True, wait_until_finish=True)
```

As an experimental customization, we also now offer the ability to specify additional
[`apt`](https://en.wikipedia.org/wiki/APT_(software)) packages that are required for your image.
As with pip, we provide a helper method `apt_requirement(name: str, version_specifier: Optional[str])` to
construct a list of apt requirements.
The first argument is the name of the package (e.g. `"texlive"` or `"vim"`) and the second optional argument is a valid version.
Omitting the version specifier is equivalent to not fixing the version.

```python
apt_requirements = [
  # Fix the version of `texlive` to `2021.20220204-1`.
  rime_client.apt_requirement("texlive", "=2021.20220204-1"),
  # We do not care about the installed version of `vim`.
  rime_client.apt_requirement("vim")
]
```

You can add these apt requirements to your `create_managed_image` request with the optional parameter `package_requirements`.
For example:

```python
builder_job = rime_client.create_managed_image("xgboost102_tensorflow", requirements, image_type=ImageType.TABULAR, package_requirements=apt_requirements)
```

### Start a Stress Test on a Managed Docker Image

Once the image has been built successfully (this will take a few minutes), you may start stress tests using
your managed image.
The following code snippet shows how you can use your `"xgboost102_tensorflow"` image.

```python
# Insert your own stress testing configuration here.
config = ...

# Kick off a stress test on the "xgboost102_tensorflow" image.
stress_test_job = rime_client.start_stress_test(test_run_config=config, rime_managed_image="xgboost102_tensorflow")

# Wait until the job has finished and print out status information.
stress_test_job.get_status(verbose=True, wait_until_finish=True)
```

### Querying for Managed Docker Images

The true power of the Managed Images feature is that it allows you to query for existing images with desired requirements.
Instead of building a new custom Docker image for each stress test, you can query the backend
for existing images that have the desired requirements.
That makes managed images much easier to use across a team.

Say you want an image with `catboost` at version `1.0.3`.
Perhaps one of your teammates has worked on a model with the same requirement or you previously built a catboost image.
To recover those images, you can first construct filters using the helper method `Client.pip_library_filter(library_name: str, fixed_version: Optional[str])`.

```python
filters = [rime_client.pip_library_filter("catboost", "1.0.3")]
```

Then, you can provide the filters as an argument to `Client.list_managed_images()`.
This is a paginated call so you can limit the number of images returned.

*Note: `list_managed_images` returns a tuple of (`images`, `next_page_token`). See the reference for more detail on the function's behavior*.
```python
images, next_page_token = rime_client.list_managed_images(pip_library_filters=filters)
```

Each element of `images` is a dictionary that contains information about all the installed pip libraries, the alias of the image, etc.
Here is a code snippet to get all the names of the images in the first page of the query result.

```python
names = [x["name"] for x in rime_client.list_managed_images(pip_library_filters=filters)[0]]
```


