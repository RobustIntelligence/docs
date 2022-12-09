# Architecture Overview

In this configuration, Robust Intelligence hosts and manages the **control plane** on behalf of your organization, and the **data plane** remains within your environment.

<img src="../../_static/diagrams/cloud.png" style="max-height:500px" />

This means that your data and models stay within your organization's cloud, and you have full control over the compute infrastructure for model testing. Results of these tests are uploaded to the Robust Intelligence cloud, where they are served by a dedicated **control plane** cluster.

By licensing the control plane from Robust Intelligence, you can greatly reduce the amount of infrastructure that you must maintain in your environment! Rather than deploying a full Kubernetes cluster, you only need to deploy a **data plane** agent for model testing, which we've made available as a single [Helm](https://helm.sh/) chart.

To begin the deployment, start by verifying the [Requirements](requirements.md).

---

## Local Agent

For rapid experimentation using local files on your personal machine (no cloud environment setup needed), the **data plane** agent can also be deployed locally! In this configuration, the agent would run on a local Kubernetes cluster (e.g., [kind](https://kind.sigs.k8s.io/) or [Minikube](https://minikube.sigs.k8s.io/)).

Note that we only recommend this configuration for exploratory purposes.

See [Local Agent](local.md) for more details on setup and usage.
