# Managed Images

Managed Images is a feature of the RI Platform that allows you to easily containerize a model's dependencies --- programmatically (e.g., via the Python SDK) specify your model's dependencies and easily swap between Docker images as you run different models!

Currently Managed Images operates via [AWS ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html).

*NOTE*: as of version 0.13.0, the Managed Images feature is enabled by default in our Terraform module.

Configuration for this feature is handled via the `image_registry_config` of the `rime` Terraform module:
```
module "rime" {
  ...
  image_registry_config = {
    enable                       = true
    allow_external_custom_images = true
    repository_prefix            = ""
  }
  ...
}
```

## `repository_prefix`

The `repository_prefix` is a string that labels your managed image repositories within ECR.

The RI Platform will operate **only** on repositories beginning with this `repository_prefix`.

## Permissions for the Managed Image Registry

Permissions for Managed Images can be applied automatically by an admin when applying our Terraform module.
```
ecr:CreateRepository
ecr:DeleteRepository
ecr:DescribeImages
ecr:PutLifecyclePolicy
ecr:ListImages
```

These permissions allow the registry server to create and modify repositories with the given `repository_prefix`. Additionally, it requires `ecr:GetAuthorizationToken` for all resources in order to authorize itself.

Jobs executed by the registry server use the following permissions to build new images:
```
ecr:BatchGetImage
ecr:BatchCheckLayerAvailability
ecr:CompleteLayerUpload
ecr:GetDownloadUrlForLayer
ecr:InitiateLayerUpload
ecr:PutImage
ecr:UploadLayerPart
```

These permissions allow these jobs to pull and push new images to the repositories created with prefix `repository_prefix`. These jobs also require `ecr:GetAuthorizationToken` for all resources in order to authorize themeselves.
