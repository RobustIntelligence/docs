# Getting Started
Once Robust Intelligence has set up your RI Platform, you can access it via the Web Client or Python SDK. 

Note that if your organization is deploying an RI Platform Agent on your own infrastructure, additional steps are needed prior to launching your first test.

## Web Client
Your RIME web client will be made available at a URL with the following form:
`https://rime.<YOUR_ORG_NAME>.rime.dev/`

### Admin User Setup
Initially, a team member from your organization will be designated as the admin user for their RIME cluster.

This user will receive an email from Robust Intelligence with steps for setting up their account.

### Adding Other Members
Once the admin user's account is configured, they will be able to grant access to other users via the *Workspace Settings*.

More detailed instructions can be found in the [User Management Guide](/for_admins/how_to_guides/users.md).

An admin can also set up SSO to use an external Identity Provider. More detailed instructions for configuration can be found in the [SSO Configuration Guide](/for_admins/how_to_guides/sso.md)

Users can login via basic authN service or SSO. Admin operations need to be performed via basic authN login.

## Python SDK
Cloud installations utilize the [RIME Python SDK](/for_data_scientists/reference/python-sdk.rst) for programmatic integration with your existing ML pipeline!

Installation is simple:
```bash
pip install rime-sdk
```

### Create an API Token
An API token is needed to access the Python SDK. These can be created in the web client via the *Workspace Settings*.

More detailed instructions can be found in the [API Authentication Guide](/for_admins/how_to_guides/api-authentication.md).

### Test Connection

Run the code snippet below to test your SDK connection:
```python
from rime_sdk import Client

rime_client = Client("rime.<YOUR_ORG_NAME>.rime.dev", "<RIME_API_TOKEN>")
```

---
## Managed Cloud

If your organization is using **RI Platform Managed Cloud**, Robust Intelligence hosts the entire RI Platform and there are no further installation steps necessary to get started!

---
## Agent Installation

Otherwise, if your organization is installing the RI Platform Agent separately on your cloud or on-premise, follow the directions below to set up an agent prior to attempting to run any tests.
- [Architecture Overview](agent/arch_overview.md)
- [System Requirements](agent/requirements.md)
- [Agent Deployment](agent/deployment.md)
- [Local Agents](agent/local.md)

---