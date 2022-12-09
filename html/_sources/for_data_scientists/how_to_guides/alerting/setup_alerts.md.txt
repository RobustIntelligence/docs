# Alerts and Notifications

Notifications make the RI Platform much more useful for data scientists.
Below, you may learn the different kinds of supported notifications and how you
can easily set them up.

## Types of Notifications 

All the following types of notifications are configured at the Project level.
You can opt into any subset.

### Monitoring Notifications
* Preferred means of learning about model health over time.
* Triggered when a single bin (i.e. a day's worth of data) of Continuous Testing completes and has failing Issues.
  * Issues are key statistics that the RI Platform tracks over time, such as Abnormality Rate,
    Prediction Drift, or Average Test Severity.
  * Issues are a proxy for model health, so you will only be alerted when your model is unhealthy.
* Configurable by toggling Thresholds for each Issue.
  * You can fine tune the thresholds or disable it entirely via the web app or the SDK.
* Default thresholds are computed from the Stress Test used to create your AI Firewall.
* Will NOT be sent if there are no failing Issues.
  * If you find a metric is too noisy and disable it, it will no longer count as "failing" and no
    notifications will be triggered unless other Issues fail.
    Disabling thresholds is a great way to avoid alert fatigue.
* Show you at a glance what the high-level problems are with your model

### Job Action Notifications
* Triggered during key status changes in the life cycle of a testing job, such as completion or failure.
* Useful for long-running jobs with large datasets / complex models.

### Daily Digest Notifications
* Include a summary of all Stress Test runs for the day.
* Will NOT be sent if there are no Stress Tests for the day.
* Sent out every day at 8am in the timezone configured 
by the default workspace (initialized to UTC).


## Configuring Notifications

### How to Configure Email Notifications

* Email notifications depend on the RIME instance having a properly [configured SMTP server](../../../for_admins/how_to_guides/smtp-configuration.md).

* Email addresses can be added by clicking on the alerts icon for a particular project in the web app or calling a method in the SDK.

  ```python
  project = rime_client.get_project("<your_project_id_here")
  # Strings for the type of the notification to sign up for are:
  # ["Job_Action", "Monitoring", "Daily_Digest"]
  project.add_email("<your_email_here>", "Monitoring")
  ```

* Currently, Gmail and Outlook are the only officially supported email clients.

* Email notifications are supported for Enterprise customers and Cloud Trial customers.

    * Enterprise customers will need to configure SMTP with their own server. SMTP settings live under workspace settings.
    
    * Cloud Trial customers will receive emails from “dev@robustintelligence.com”. Add this email address to your safe senders list to prevent it from going to spam.
    
* Emails can be removed from a project in the web app or the SDK.

  ```python
  project = rime_client.get_project("<your_project_id_here")
  project.remove_email("<your_email_here>")
  ```

### How to Configure Webhooks

* Arbitrary webhook URLs may be added by clicking the alerts icon for a particular project on the web app or by calling a method in the SDK.

  ```python
  project = rime_client.get_project("<your_project_id_here")
  # Strings for the type of the notification to sign up for are:
  # ["Job_Action", "Monitoring", "Daily_Digest"]
  project.add_webhook("<your_webhook_url_here", "Job_Action")
  ```
* Webhook URLs should be preauthenticated (i.e. include a security token as a URL parameter).
  After you create a webhook from another application to copy-paste into the RI Platform, ensure
  that you do not share that webhook publicly.

* Webhooks can be removed from a project in the web app or the SDK.

  ```python
  project = rime_client.get_project("<your_project_id_here")
  project.remove_webhook("<your_webhook_url_here")
  ```

### How to Configure Slack Notifications

* Incoming webhooks are the preferred way to integrate Slack and the RI Platform.

* Create an Incoming Webhook Slack App using the instructions [here](https://api.slack.com/messaging/webhooks).

* Use the instructions for configuring webhooks above to add your created webhook to your project of choice.

### How to Configure Monitoring Thresholds

* Thresholds are important because they determine whether Monitoring notifications will be sent for particular Continuous
  Testing runs.
* You can manually tune and disable thresholds in the web app by navigating to the "Continuous Tests" page and clicking on the icon
  in the top left of the graph.
  Be sure to click "Save" so that your changes are reflected!

<img src="../../../_static/configure_thresholds_demo.png">

* Thresholds can also be modified in the SDK.

  ```python
  project = rime_client.get_project("<your_project_id_here")
  firewall = project.get_firewall()
  
  # Get a pd.DataFrame with the current thresholds.
  df = firewall.get_metric_thresholds()
  
  # Disable the threshold for "Abnormality Rate"
  firewall.update_metric_thresholds("Abnormality Rate", disabled=True)
  ```