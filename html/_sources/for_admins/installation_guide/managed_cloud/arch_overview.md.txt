# Architecture Overview

In this configuration, Robust Intelligence hosts and manages **both planes** in a dedicated environment for your organization.

<img src="../../../_static/diagrams/managed_cloud.png" style="max-height:500px" />

This means that you **do not have to manage any infrastructure, period**. No need to configure instances or allocate IP addresses!

Robust Intelligence will provision an isolated Kubernetes cluster for your organization, where data and models will be encrypted in our private storage. All model testing will execute on dedicated instances, with neither data nor metadata travelling outside of the VPC.

This configuration requires no deployment! Here are some setup steps you can take to begin using the RI Platform for your team:
- [User Management](/for_admins/how_to_guides/users.md)
- [SSO Configuration](/for_admins/how_to_guides/sso.md)

Once your users log in, they can follow the standard onboarding process outlined in the main "Get Started" section:
- [Get Started](/for_data_scientists/get_started.rst)

