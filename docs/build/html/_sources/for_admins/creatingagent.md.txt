# Creating a Managed Agent

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
    | Local       | Creating a local Managed Agent          |
    | Amazon EKS  | Creating an Amazon EKS Managed Agent    |
    | Google GKE  | Creating a Google GKE Managed Agent     |

## Creating a local Managed Agent

Before you begin, finish the procedure described in Creating a Managed Agent. Set up a local Kubernetes cluster.

1.  In *Agent Name*, type a name for the managed agent.
2.  Unfold the *Download Helm Values File* section and click *Download Values File*.
    >   The values file is a YAML-format text file.
3.  Unfold the *Run Helm Commands* section and click the icon at the top right to copy the two command-line instructions to the clipboard.
4.  Paste and execute the commands at the command line.
    >   The commands add the Robust Intelligence repo to Helm and install the Agent Helm chart.

The Managed Agent is ready for use.

## Creating an Amazon EKS Managed Agent

Before you begin, finish the procedure described in Creating a Managed Agent. Verify access to an EKS cluster and an AWS IAM role with S3 access.

1.  In *Agent Name*, type a name for the managed agent.
2.  In *AWS Role ARN for S3 Access*, type the ARN.
3.  Unfold the *Download Helm Values File* section and click *Download Values File*.
    >   The values file is a YAML-format text file.
4.  Unfold the *Run Helm Commands* section and click the icon at the top right to copy the two command-line instructions to the clipboard.
5.  Paste and execute the commands at the command line.
    >   The commands add the Robust Intelligence repo to Helm and install the Agent Helm chart.

The Managed Agent is ready for use.

## Creating a Google GKE Managed Agent

Before you begin, finish the procedure described in Creating a Managed Agent. Verify access to a GKE cluster and a GCP Service Account with GCS access.

1.  In *Agent Name*, type a name for the managed agent.
2.  In *GCP Service Account Email*, type the email address associated with the GCP Service Account.
2.  Unfold the *Download Helm Values File* section and click *Download Values File*.
    >   The values file is a YAML-format text file.
3.  Unfold the *Run Helm Commands* section and click the icon at the top right to copy the two command-line instructions to the clipboard.
4.  Paste and execute the commands at the command line.
    >   The commands add the Robust Intelligence repo to Helm and install the Agent Helm chart.

The Managed Agent is ready for use.