# Upgrading the Agent

At Robust Intelligence, we are constantly working to improve our platform to create more value for our customers. Whenever we release a new version of the product, we will notify your team and work together to schedule an upgrade.

For the Cloud configuration, Robust Intelligence will schedule an upgrade with you to ensure that the **control plane** is upgraded in sync with your **data plane** agent.

## Helm Upgrade

Upgrading is as simple as re-running the [original installation command](/for_admins/installation_guide/cloud/deployment.md) with a different value for the `--version` parameter (replace <NEW_VERSION> in the command below):
```shell
helm upgrade -i rime-agent robustintelligence/rime-agent --version <NEW_VERSION> --values <PATH TO DOWNLOADED VALUES FILE>
```
