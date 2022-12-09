# System Requirements

To help organize the information, we've broken down requirements into four categories:
- **Tools** (utilities we use for deploying or maintaining the cluster)
- **Resources** (consumable, measurable artifacts like S3 buckets)
- **Permissions** (access needed to perform deployment/maintenance actions)
- **Information** (values we must know when deploying or maintaining the cluster, often involve making configuration decisions)

The lists below are meant to provide a working understanding of what is needed for deployment; however, we will work with your team to tailor a more comprehensive list beforehand based on your infrastructure needs.

## Tools
- Terraform v1.0.2 or above ([install](https://learn.hashicorp.com/tutorials/terraform/install-cli))
- Helm 3.6.1 or above ([install](https://helm.sh/docs/intro/install/))
- AWS CLI 2.2.29 or above ([install](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html))
    - Setup your AWS config & credentials.
    - Test that awscli works e.g. by trying to list your S3 buckets:
        ```bash
        aws s3api list-buckets
        ```
- Kubernetes CLI 1.20 or above ([install](https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html))

## Resources
- VPC x 1
  - Private Subnet x 2 (recommended at least 50 IP addresses per subnet)
  - Public Subnet x 2 (recommended at least 10 IP addresses per subnet)
- S3 bucket x 3 (can add more as needed)
- EC2 instances x 4 (can scale up as needed)
  - 3 for **control plane** services
    - recommended at least 8 GiB RAM
  - 1 for **data plane** services
    - recommended at least 16 GiB RAM
- 2 Network Load Balancers
- 2 SSL Certificates
- 2 Domains
  - 1 with a `rime` sub-domain
  - 1 with a `rime-backend` sub-domain

## Permissions
NOTE: Robust Intelligence will provide you with an updated list of specific IAM resources before deployment.
- Administrator IAM Role
  - for creating and destroying resources for the cluster
- Model Testing Service-Linked IAM Role
  - for the cluster to read models and data
- Cluster Autoscaler IAM Role (Optional)
  - for EKS to automatically scale up the cluster
- External DNS IAM Role (Optional)
  - for modifying DNS records in Route 53
- Elastic Load Balancer Service-Linked IAM Role (Optional)
  - for managing Network Load Balancers
- Blob Storage Service-Linked IAM Role (Optional)
  - for the cluster to read/write models and data to/from a dedicated S3 bucket
- ECR Image Builder Service-Linked IAM Role (Optional)
  - for the cluster to build custom Docker images for containerizing model dependenceies
- ECR Repo Manager Service-Linked IAM Role (Optional)
  - for the cluster to push custom Docker images for containerizing model dependenceies

## Information
- Desired AWS region(s)
- Desired custom integrations (we will help you decide)
- Designated cluster administrator email
- Data Science team emails (to create their accounts)
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
