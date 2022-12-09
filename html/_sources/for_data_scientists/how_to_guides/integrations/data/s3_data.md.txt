# s3

It is common to store data in s3. RIME supports loading data directly from s3 so you do not have to copy the file locally.


Follow all of the instructions in the generic [Data Configuration](/for_data_scientists/reference/tabular/data_source.md) guide, except the path to the data should no longer be a local path but instead an s3 storage path in the format of `s3://{bucket_name}/{object_key}`. Note that `bucket_name` and `object_key` should be replaced so they reference the desired csv or parquet file.

Example:
```
{
    "data_info": {"ref_path": "s3://my-bucket/my-file.csv"}
}
```
