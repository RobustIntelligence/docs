# System Requirements

Requirements for installing RIME are listed in the following categories:

<dl>
  <dt></strong>Tools</strong></dt>
    <dd>utilities for deploying or maintaining the cluster</dd>
  <dt><strong>Resources</strong></dt>
    <dd>consumable, measurable artifacts such as S3 buckets</dd>
  <dt><strong>Permissions</strong></dt>
    <dd>privileges required to perform deployment or maintenance actions</dd>
  <dt><strong>Information</strong></dt>
    <dd>values that must be defined on the system, which vary based on specific configurations</dd>
</dl>

The following information provides a working understanding of deployment requirements.
RIME staff can work with your team to generate a comprehensive list based on your
specific infrastructure needs.

## Tools
- Terraform v1.0.2 or above ([install](https://learn.hashicorp.com/tutorials/terraform/install-cli))
- Helm 3.6.1 or above ([install](https://helm.sh/docs/intro/install/))
- AWS CLI 2.2.29 or above ([install](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html))
    - Set up your AWS config & credentials.
    - Test that `awscli` works by trying to list your S3 buckets:
        ```bash
        aws s3api list-buckets
        ```
- Kubernetes CLI 1.20 or above ([install](https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html))

## Resources
All resource specifications are approximate. Actual resource requirements will vary
with your specific use case.
- VPC x 1
  - Private Subnet x 2 (recommended at least 50 IP addresses per subnet)
  - Public Subnet x 2 (recommended at least 10 IP addresses per subnet)
- S3 bucket x 3 (can add more as needed)
- EC2 instances x 5* (can scale up as needed)
  - 4 for **control plane** services
    - At least 16 GiB of RAM are recommended in an Autoscaling group. The `t3.xlarge`
    size is suitable.
  - 1 for **data plane** services
    - At least 16 GiB of RAM are recommended in an Autoscaling group. The `t3.xlarge`
    size is suitable.
- 2 Network Load Balancers
  - (NOTE: these are auto-provisioned by the Ingress services)
- 2 SSL Certificates
- 2 Domains
  - 1 with a `rime` sub-domain
  - 1 with a `rime-backend` sub-domain

## Permissions
Robust Intelligence provides you with an updated list of specific IAM resources before deployment.
- Administrator IAM Role
  - to create and destroy cluster resources
- Model Testing Service-Linked IAM Role
  - to enable the cluster to read models and data
- Cluster Autoscaler IAM Role (Optional)
  - to enable EKS to automatically scale up the cluster
- External DNS IAM Role (Optional)
  - to modify DNS records in Route 53
- Elastic Load Balancer Service-Linked IAM Role (Optional)
  - to manage network load balancers
- Blob Storage Service-Linked IAM Role (Optional)
  - to enable the cluster to read and write models and data to and from a dedicated S3 bucket
- ECR Image Builder Service-Linked IAM Role (Optional)
  - to enable the cluster to build custom Docker images in order to containerize model dependencies
- ECR Repo Manager Service-Linked IAM Role (Optional)
  - to enable the cluster to push custom Docker images in order to containerize model dependencies

## Information
- Desired AWS region or regions.
- Desired custom integrations. RIME staff is available to assist in determining which custom integrations to use.
- Designated cluster administrator email address.
- Email addresses of the Data Science team members, in order to create the respective accounts.
- OIDC Configuration Values (Optional)
  - Client ID
  - Client Secret
  - Issuer URL
  - Callback URL
- SMTP Configuration Values (Optional)
  - Server URL and port
  - Sender address
  - Sender address secret
  - Receiver address(es)
