# Uploading Data to RIME

You can use the SDK to upload data files and model directories to a s3 bucket 
that RIME has permission to use.


## Uploading Data Files

{{ sdk_client_setup }}

Afterwards, data can easily be uploaded using the `upload_file(file_path, upload_path)` method.

If the `upload_path` is not specified, the path will contain a random string as directory name.
```python
ref_path = rime_client.upload_file(file_path="./titanic/datasets/train.csv")
print("ref_path:", ref_path)
"ref_path: s3://rime-blob-c78976e9367daf-environment/files/84f82c37-0d8f-43af-8d05-76jknwefnjkm/data/train.csv"
```

If the `upload_path` is  specified, the path will contain the `upload_path` string in place of the random string.
```python
ref_path = client.upload_file(file_path="./titanic/datasets/train.csv", upload_path="rime_tests/titanic_tests")
print("ref_path:", ref_path)
"ref_path: s3://rime-blob-c78976e9367daf-environment/files/rime_tests/titanic_tests/data/train.csv"
```

## Uploading Model Directories
The model directory is a directory containing the `model.py` file and any 
extras (e.g.: pre-processing code, the pickle file) that the `model.py`  file depends on.  

Model directories can easily be uploaded using the `upload_directory(file_path, upload_hidden, upload_path)` method.

If the `upload_path` is not specified, the path will contain a random string as directory name.
```python
model_dir = rime_client.upload_directory(dir_path="./titanic/model")
print("model_dir:", model_dir)
"model_dir: s3://rime-blob-c78976e9367daf-environment/files/c83aa17d-709b-48b5-89ed-a9e4bad42f0b/model"
```

If the `upload_path` is  specified, the path will contain the `upload_path` string in place of the random string.
```python
model_dir = client.upload_directory(dir_path="./titanic/model", upload_path="rime_tests/titanic_tests")
print("ref_path:", ref_path)
"model_dir: s3://rime-blob-c78976e9367daf-environment/files/rime_tests/titanic_tests/model"
```