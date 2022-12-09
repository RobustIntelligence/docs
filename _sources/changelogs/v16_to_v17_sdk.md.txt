# RIME v17 SDK Breaking Changes 

#### This is a guide on how to port your v16-based SDK code to v17 SDK.

### Sample Notebooks
 - Compare the <a class="reference external" href="https://colab.research.google.com/drive/13g7PO-ObLt_BOO58rF-N_Sk7ursi0bHu#scrollTo=LhYmw2kM0ebb" target="_blank">v16 notebook (previous release)</a>
  and the <a class="reference external" href="https://colab.research.google.com/drive/1o_jG_Z0Mxd5lqXN2pvaH9OT3_4u-bhKT" target="_blank">v17 notebook (current release)</a>
  to understand the differences in user experience. 

### Class Name Changes 
- The SDK class names have been renamed to avoid "RIME".
```python
  #v16 
  from rime_sdk import RIMEClient, RIMEStressTestJob, RIMEProject, RIMEFirewall 
  
  #v17 improvement
  from rime_sdk import Client, Project, Job, TestRun, Firewall 
```
  
### Authentication
- Authentication errors are thrown when you establish the client as opposed to when you use the client.
```python
  #v16 
  rime_client = RIMEClient(CLUSTER_URL, API_TOKEN)
  project =   rime_client.create_project(name = "", description = "")
  "Unauthenticated API error"
  
  #v17 improvement
  client = Client(CLUSTER_URL, API_TOKEN)
  "Unauthenticated API error"
```

### Project Class Enhancements 
- Firewall CRUD operations have moved from the client to project class.
- Ability to list test runs part of a project.
```python
  #v16 
  project =  rime_client.create_project(name = "", description = "")
  rime_client.create_firewall(name = "", bin_size_seconds = "", test_run_id = "", project_id = "")
  firewall = rime_client.get_firewall_for_project(project_id="")
  
  #v17 improvement
  project =  client.create_project(name = "", description = "")
  project.create_firewall(name = "", bin_size = "", test_run_id = "")
  firewall = project.get_firewall()
```
  
### Firewall Creation
- When creating a firewall, you specify the bin size as a string as opposed to bin size in seconds float value.
```python
  #v16 
  rime_client.create_firewall(name = "", bin_size_seconds = "=60*60", test_run_id = "", project_id = "")
  rime_client.create_firewall(name = "", bin_size_seconds = "=60*60*24", test_run_id = "", project_id = "")

  #v17 improvement
  project.create_firewall(name = "", bin_size = "hour", test_run_id = "")
  project.create_firewall(name = "", bin_size = "day", test_run_id = "")
```

### Job and TestRun classes
- The SDK now has Job and TestRun classes.
- The Job class is used to track the status of a job that has been kicked off.
- The TestRun class is used after a job has successfully completed and you want to access 
the results or the test run. 
```python
  #v16 
  stress_job = rime_client.start_stress_test(test_run_config = "", project_id = "")
  stress_job.get_status(verbose = "", wait_until_finish = "")
  rime_client.list_stress_test_jobs()
  stress_job.get_link()
  stress_job.get_test_run_result()
  
  
  #v17 improvement
  job = client.start_stress_test(test_run_config = "", project_id = "")
  job.get_status(verbose = "", wait_until_finish = "")
  client.list_stress_test_jobs()
  project.list_test_runs()
  test_run = job.get_test_run()
  test_run.get_link()
  test_run.get_result_df()
```

### Querying Capabilities
 - Results are queried from the TestRun class as opposed to the Job class. 
 - Querying method names have changed.
  ```python
  #v16 
  stress_job = rime_client.start_stress_test(test_run_config = "", project_id = "") 
  stress_job.get_test_run_result()
  stress_job.get_test_cases_result()
  
  #v17 improvement
  job = rime_client.start_stress_test(test_run_config = "", project_id = "")
  test_run = job.get_test_run()
  test_run.get_result_df()
  test_run.get_test_cases_df()
  ```


  