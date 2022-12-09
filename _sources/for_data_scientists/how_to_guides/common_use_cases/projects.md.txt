# Projects

An RI Platform project collects test runs or an AI Firewall that relate to a shared machine learning task.
Each model for the task is tested by an individual test run. An AI Firewall monitors a currently promoted
model over time by continuously testing that model.

## Creating a Project

You can use the RI Platform SDK or the RI Platform web UI to create a new project.

### With the RI Platform SDK

Verify that the SDK client is initialized. If necessary, initialize the SDK client now.

{{ sdk_client_setup }}

Create a project by calling the `create_project()` method, which returns a `Project` object.

```python
project = rime_client.create_project("<NAME>", "<DESCRIPTION>")
```

### Configuring a Stress Testing project from the RI Platform web UI

1.  Sign in to a RI Platform instance.  
    >    The Workspaces page appears.
2.  Click a workspace.  
    >    The Workspaces summary page appears.
3.  Click *Create New Project*.
    >   The Create New Project dialog box appears.
4.  In *Name*, type a name for the new project.
5.  (Optional) In *Brief Description*, type a description of the new project.
6.  Click *Stress Testing*.

The Stress Testing project is ready.

### Configuring a Continuous Testing project from the RI Platform web UI

1.  Sign in to a RI Platform instance.  
    >   The Workspaces page appears.
2.  Click a workspace.  
    >   The Workspaces summary page appears.
3.  Click *Create New Project*.
    >   The Create New Project dialog box appears.
4.  In *Name*, type a name for the new project.
5.  (Optional) In *Brief Description*, type a description of the new project.
6.  Click *Continuous Testing*.
    >   The Set up Continuous Testing page appears.
7.  Click *Activate*.
    >   The Set Up Continuous Tests and Firewall dialog box appears.
8.  In *Name*, enter a name for the test.
9.  From the *Modality* drop-down, select a test modality.
10. From the *Task* drop-down, select a task.
11. (Optional) In *Model Path*, type a path to the model file.
12. Make selections from the following drop-downs:
        - *Reference Set*
        - *Data Source*
        - *Connection*
        - *Table Name*
13. In *Label Column*, type the name of the label column.
14. In *Prediction Column*, type the name of the prediction column. 
15. In *Timestamp Column*, type the name of the timestamp column.
16. Click *Finish*.

The Continuous Testing project is ready.  

## Project management operations

A user with the required privilege level can rename or delete existing projects, or move test runs between existing projects.

### Renaming a project

1.  Sign in to a RI Platform instance.  
    >   The Workspaces page appears.
2.  Click a workspace.  
    >   The Workspaces summary page appears.
3.  Select a project.
    >   You can filter or sort the list of projects in a workspace with the
    >   *Sort* and *Filter* controls in the upper right. Click the glyph to the
    >   right of the *Filter* control to switch between list and card display
    >   for projects. Type a string in *Search Projects...* to display only
    >   projects that match the string.
    >   The project overview page appears.
4.  Click the gear at the upper right.
    >   The Edit Continuous Tests and Firewall dialog box appears.
5.  In *Name*, type the new project name.
6.  Click *Save*.

The project name is changed.

### Deleting a project

1.  Sign in to a RI Platform instance.  
    >   The Workspaces page appears.
2.  Click a workspace.  
    >   The Workspaces summary page appears.
3.  Select a set of projects.
    >   The Delete option appears above the list of prjects.
4.  Click *Delete*.
    >   A confirmation dialog box appears.
5.  Click *Remove*.

The selected projects are removed from the workspace.

### Moving test runs between projects

1.  Sign in to a RI Platform instance.  
    >   The Workspaces page appears.
2.  Click a workspace.  
    >   The Workspaces summary page appears.
3.  Select a project.
    >   You can filter or sort the list of projects in a workspace with the
    >   *Sort* and *Filter* controls in the upper right. Click the glyph to the
    >   right of the *Filter* control to switch between list and card display
    >   for projects. Type a string in *Search Projects...* to display only
    >   projects that match the string.
    >   The project overview page appears.
4.  From the left-hand navigation bar, select the *AI Stress Tests* icon.
    >   A table of test runs appears.
5.  Select a set of test runs.
    >   The Move to Project and Delete options appear above the table of test runs.
6.  Click *Move to Project*.
    >   The Move to Project dialog box appears.
7.  Select a project.
    >   Type a string in *Search Projects...* to display only
    >   projects that match the string.
8.  Click *Move*.

The selected test runs move to the specified project.

### Setting up project alerts

1.  Sign in to a RI Platform instance.  
    >   The Workspaces page appears.
2.  Click a workspace.  
    >   The Workspaces summary page appears.
3.  Select a project.
    >   You can filter or sort the list of projects in a workspace with the
    >   *Sort* and *Filter* controls in the upper right. Click the glyph to the
    >   right of the *Filter* control to switch between list and card display
    >   for projects. Type a string in *Search Projects...* to display only
    >   projects that match the string.
    >   The project overview page appears.
4.  Click the gear at the upper right.
    >   The Edit Continuous Tests and Firewall dialog box appears.
5.  Click *Set up Alerts*.
    >   The Alerts fields unfold.
6.  Choose an alert delivery model.
    | Alert delivery | Configuration step                                             |
    |----------------|----------------------------------------------------------------|
    | Email          | In *Email Address*, type an email address and click *Add*.     |
    | Slack          | In *Webhook URL*, paste the Slack webhook URL and click *Add*. |

    [Slack documentation](https://api.slack.com/messaging/webhooks) provides details on generating a Slack webhook URL.
7.  Click *Confirm*.

Alerts are configured for this project.
