# Data Sources Configuration

* Administrators can configure data sources using the UI from the "Data Sources" 
page under the "Organization Settings". You can see how in the below image.
* Sensitive information such as access tokens will be securely stored in a 
secret manager service built on top of Hashicorp Vault. 
* Supported Data Sources - [Databricks Deltalake](/for_data_scientists/how_to_guides/integrations/data/databricks_deltalake.md)
* Note: 
  * Native cloud stores like S3 and Google Cloud Storage are also supported.
  However, they can only be configured during deployment and not via the UI. 

<img src="../../_static/data-sources.png">
<img src="../../_static/delta-lake.png">