# Agent Configuration

Agent configuration can be handled in the settings section of the RI Platform's web client.

Note that only administrators (see [User Management](/for_admins/how_to_guides/users.md)) have permissions to manage agents.

<img src="../../../_static/agent-configuration-1.png" />

Click the "Create Agent" button on the right to get started. This will open up a form.

<img src="../../../_static/agent-configuration-2.png" />

Toggle for the agent type that corresponds to your setup ("Local" or "Amazon EKS") and fill out the details accordingly.

For "Amazon EKS" configuration, the ARN for S3 access should correspond to the IAM role for the agent's service account (see [Requirements](/for_admins/installation_guide/cloud/requirements.md) for more details).

<img src="../../../_static/agent-configuration-3.png" />

Once you have completed the form, you will receive some Helm commands --- copy these and proceed to [Deploying the Agent](/for_admins/installation_guide/cloud/deployment.md).
