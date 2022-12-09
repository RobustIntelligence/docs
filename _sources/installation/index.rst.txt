Installation Guide
================================

The RI Platform is deployed as a Kubernetes cluster with two conceptual entities: a **control plane** and a **data plane**.

.. raw:: html

   <img src="../_static/diagrams/cluster_only.png" style="max-height:450px"/>

The **control plane** consists of core application services like the web server and user management.

The **data plane** executes the machine learning testing suite on your models and data, generating test results for the control plane to serve to users.

These two entities can be deployed in multiple configurations, depending on your organization's needs.

.. TODO add a lean table that compares the 3 options

Managed Cloud
````````````````````````````````
.. TODO Add a page regarding anonymization, when available!

In this configuration, Robust Intelligence hosts and manages **both planes** in a dedicated environment for your organization.

.. toctree::
   :maxdepth: 1

   managed_cloud/arch_overview.md

Self-Hosted
````````````````````````````````

In this configuration, **both planes** are hosted in your organization’s private cloud.

.. toctree::
   :maxdepth: 1

   self_hosted/arch_overview.md
   self_hosted/requirements.md
   self_hosted/configuration.md
   self_hosted/deployment.md
   self_hosted/upgrade.md

Cloud
````````````````````````````````

In this configuration, Robust Intelligence hosts and manages the **control plane** on behalf of your organization, and the **data plane** remains within your environment.

.. toctree::
   :maxdepth: 1

   cloud/arch_overview.md
   cloud/requirements.md
   cloud/agent_configuration.md
   cloud/deployment.md
   cloud/upgrade.md
   cloud/local.md


