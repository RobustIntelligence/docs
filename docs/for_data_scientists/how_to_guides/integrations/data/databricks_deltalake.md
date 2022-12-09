# Databricks Deltalake

RIME now supports loading data directly from Databricks Deltalake directly, 
so you do not have to copy the file locally or to s3. You can configure
[Databricks Deltalake using the UI.](/for_admins/how_to_guides/data-sources.md)

**In order to configure the Databricks Deltalake, you need to enter the following information -**
1) Connection Details - Server Hostname, HTTP Path
2) Databricks Access Tok


**In order to get the Databricks Deltalake connection details -** 
1) Click compute icon in the sidebar. 
2) Choose a cluster to connect to. 
3) Navigate to Advanced Options. 
4) Click on the JDBC/ODBC tab. 
5) Copy the above connection details.


After the data source is configured, you can use the underlying delta tables
to run stress tests and continuous tests. More information for how to define 
the configurations can be found in the 
[Data Configuration page](/for_data_scientists/reference/tabular/data_source.md).
Additionally, information about how to integrate the delta tables into your
Scheduled CT workflow can be found in the [Scheduled CT Configuration page](/for_data_scientists/reference/tabular/scheduled_ct_configuration.md).

 
 