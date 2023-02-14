# Requirements

These are requirements for installing the **data plane** agent into your organization's cloud. Instructions for installating a local agent can be found [here](local.md).

## Prerequisites

- [Helm](https://helm.sh/docs/intro/install/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)

## Kubernetes Cluster

The **data plane** agent is installed via Helm on your Kubernetes cluster.

- You (the admin) must have proper permissions to interact with the cluster via Helm and `kubectl`.
- Recommended to have nodes with 16GiB+ memory. For AWS EC2, this would be a `xlarge` instances.
- Cluster must allow containers to make external network calls to the RI Platform.
- Cluster must have nodes that the agent and launched jobs can be scheduled on (i.e. without NoSchedule taints).

Robust Intelligence can provide assistance in setting up your cluster.

## Data Access Permissions

The **data plane** agent uses a K8s service account for read access to the data and models you wish to use.

### AWS EKS + S3

First, create an IAM role that the service account can assume.
- [IAM roles for service accounts](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html)

If not already configured for your cluster, be sure to create an IAM OIDC provider for your cluster to use IAM roles for service accounts.
- [Creating an IAM OIDC provider for your cluster](https://docs.aws.amazon.com/eks/latest/userguide/enable-iam-roles-for-service-accounts.html)

Additionally, be sure to create a service account and connect it to an IAM role with following policy. This ensures the agent has read access to the appropriate S3 bucket(s).
- [Configuring a Kubernetes service account to assume an IAM role](https://docs.aws.amazon.com/eks/latest/userguide/associate-service-account-role.html)
- **data plane** agent S3 Bucket read policy:
    ```json
    {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "s3:ListBucket"
              ],
              "Resource": "arn:aws:s3:::<YOUR_BUCKET>"
          },
          {
              "Effect": "Allow",
              "Action": [
                  "s3:GetObject"
              ],
              "Resource": "arn:aws:s3:::<YOUR_BUCKET>/*"
          }
      ]
    }
    ```

### Other Cloud Providers

If you are using a different cloud provider or want to specify the service account directly, you can specify other configurations via the `rimeAgent.modelTestJob.serviceAccount` helm values. A Robust Intelligence team member can help you through this process.

