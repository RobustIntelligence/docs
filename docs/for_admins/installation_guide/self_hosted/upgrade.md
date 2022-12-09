# Upgrading Your RI Platform Cluster

At Robust Intelligence, we are constantly working to improve our platform to create more value for our customers. Whenever we release a new version of the product, we will notify your team and work together to schedule an upgrade.

## Terraform Apply

The RI Platform upgrade process is generally quite simple --- update the two references to the product version (indicated below) and then re-apply!

### `main.tf`

In your configuration, replace the version declarations in `source` and `rime_version`.

```terraform
module "rime" {

  source = "https://github.com/RobustIntelligence/terraform/archive/refs/tags/<NEW_VERSION>.tar.gz"

  rime_version = "<NEW_VERSION>"

  ...

}
```

Once complete, simply refresh metadata and re-apply:
1. Refresh Helm chart and Terraform metadata.
  ```shell
  helm repo update
  terraform get -update
  ```
2. Re-apply Terraform.
  ```shell
  terraform apply
  ```

---

## For Private Registries

Note that if you are using a private registry to mirror artifacts, you will need to push updated images before re-applying Terraform. Robust Intelligence will send you an updated list of dependencies beforehand so you can update your registry accordingly!
