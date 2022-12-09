# Create and Manage Projects

You can create projects in RIME to organize your test runs. Test runs are stored in a "default" project when a project is not specified.

## Creating a project

Creating a project can be done via SDK.

{{ sdk_client_setup }}

Afterwards, projects can be easily created using the `create_project()` method, which will return a `Project` object.

```python
project = rime_client.create_project("<NAME>", "<DESCRIPTION>")
```

## Other operations with a project

Other operations can all be done via the UI. These operations are:
- Renaming projects
- Deleting projects
- Moving test runs from one project to another
