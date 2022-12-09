# Managing agents

A managed agent is a lightweight Kubernetes deployment that runs testing jobs
within a [workspace](workspaces.md). A workspace must be assigned at least one
agent, and a given agent can be assigned to multiple workspaces. A workspace
must have a default agent specified. Jobs are run with the default agent when
an agent is not specified for that job.

Agent creation and management is restricted to users with the Organization
Administrator [role](userroles.md).

Agent configuration during deploy is discussed in [Agent Configuration](../installation/cloud/agent_configuration.md).



## Viewing the managed agent status page

The managed agent status page is available to all members of a workspace and displays the status of all agents assigned to the workspace.

1.  Sign in to a user account that has administrative privileges for an RI
    Platform instance.  
    >   The Workspaces page appears.
2.  Select a workspace.
    >   The Workspace summary page appears.
3.  Click the *Settings* icon in the lower left corner.
    >   The Workspace page appears.
4.  Click *Agent Status*.

The list of agents assigned to this workspace appears, along with the status of each agent.

## Creating a managed agent

1.  Sign in to a user account that has administrative privileges for an RI
    Platform instance.  
    >   The Workspaces page appears.
2.  Click the *Settings* icon in the lower left corner.
    >   The Organization Settings page appears.
3.  Click *Manage Agent Setup*.
    >   The Agents Setup pane appears.
4.  Click *Create Agent*.
    >   The Create Agent dialog box appears.
5.  Choose an agent type.
    | Type        | Next step                               |
    |-------------|-----------------------------------------|
    | Local       | Creating a local managed agent          |
    | Amazon EKS  | Creating an Amazon EKS managed agent    |
    | Google GKE  | Creating a Google GKE managed agent     |

### Creating a local managed agent

Before you begin, finish the procedure described in **Creating a managed agent**. Set up a local Kubernetes cluster.

1.  In *Agent Name*, type a name for the managed agent.
2.  Unfold the *Download Helm Values File* section and click *Download Values File*.
    >   The values file is a YAML-format text file.
3.  Unfold the *Run Helm Commands* section and click the icon at the top right to copy the two command-line instructions to the clipboard.
4.  Paste and execute the commands at the command line.
    >   The commands add the Robust Intelligence repo to Helm and install the Agent Helm chart.

The managed agent is ready for use.

### Creating an Amazon EKS managed agent

Before you begin, finish the procedure described in **Creating a managed agent**. Verify access to an EKS cluster and an AWS IAM role with S3 access.

1.  In *Agent Name*, type a name for the managed agent.
2.  In *AWS Role ARN for S3 Access*, type the ARN.
3.  Unfold the *Download Helm Values File* section and click *Download Values File*.
    >   The values file is a YAML-format text file.
4.  Unfold the *Run Helm Commands* section and click the icon at the top right to copy the two command-line instructions to the clipboard.
5.  Paste and execute the commands at the command line.
    >   The commands add the Robust Intelligence repo to Helm and install the Agent Helm chart.

The managed agent is ready for use.

### Creating a Google GKE managed agent

Before you begin, finish the procedure described in **Creating a managed agent**. Verify access to a GKE cluster and a GCP Service Account with GCS access.

1.  In *Agent Name*, type a name for the managed agent.
2.  In *GCP Service Account Email*, type the email address associated with the GCP Service Account.
2.  Unfold the *Download Helm Values File* section and click *Download Values File*.
    >   The values file is a YAML-format text file.
3.  Unfold the *Run Helm Commands* section and click the icon at the top right to copy the two command-line instructions to the clipboard.
4.  Paste and execute the commands at the command line.
    >   The commands add the Robust Intelligence repo to Helm and install the Agent Helm chart.

The managed agent is ready for use.

## Deactivating a managed agent

Deactivated managed agents are not removed from the RI Platform instance.

1.  Sign in to a user account that has administrative privileges for an RI
    Platform instance.  
    >   The Workspaces page appears.
2.  Click the *Settings* icon in the lower left corner.
    >   The Organization Settings page appears.
3.  Click *Manage Agent Setup*.
    >   The Agents Setup pane appears.
4.  From the three-dot menu to the right of an agent, select *Deactivate*.
    >   A confirmation dialog box appears.
5.  Click *Deactivate Agent*.

The managed agent is now inactive.

## Removing a deactivated managed agent

Managed agents must be deactivated before being removed from the RI Platform instance.

1.  Sign in to a user account that has administrative privileges for an RI
    Platform instance.  
    >   The Workspaces page appears.
2.  Click the *Settings* icon in the lower left corner.
    >   The Organization Settings page appears.
3.  Click *Manage Agent Setup*.
    >   The Agents Setup pane appears.
4.  From the three-dot menu to the right of a deactivated agent, select *Remove*.
    >   A confirmation dialog box appears.
5.  Click *Remove agent*.

The managed agent is removed from the RI Platform instance.