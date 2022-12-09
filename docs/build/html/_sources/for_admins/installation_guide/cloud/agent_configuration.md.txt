# Agent Configuration

Agent configuration is handled in the organization settings section of the RI Platform's web client. Agents are created at the organization level and can be assigned to one or more workspaces.

Note that only organization administrators (see [User Management](/for_admins/how_to_guides/users.md)) have permissions to create and edit agents.

<img src="../../../_static/agent-configuration-1.png" />

Click the "Create Agent" button on the right to get started. This will open up a form.

<img src="../../../_static/agent-configuration-2.png" />

Toggle for the agent type that corresponds to your setup ("Local" or "Amazon EKS") and fill out the details accordingly.

For "Amazon EKS" configuration, the ARN for S3 access should correspond to the IAM role for the agent's service account (see [Requirements](/for_admins/installation_guide/cloud/requirements.md) for more details).

<img src="../../../_static/agent-configuration-3.png" />

Once you have completed the form, you will receive some Helm commands --- copy these and proceed to [Deploying the Agent](/for_admins/installation_guide/cloud/deployment.md).
