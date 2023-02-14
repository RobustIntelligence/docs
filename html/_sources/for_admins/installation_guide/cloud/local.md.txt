# Local Agent

The RI Platform Agent can be installed on a local Kubernetes cluster using Kind or Minikube.

## Reasons to Use a Local Agent

- The local agent runs on your machine. You do not need access to a Kubernetes cluster running on your organization's cloud.
- Running locally also gives you full access and observability into the running tests for easy debugging and insight into resource usage.
- The local agent can use data and model files from your local file system. You do not need to upload the data to cloud storage or grant the agent permissions to read from cloud storage.

## Setting up your Local Cluster

### Prerequisites

- Directory on your local file system that will contain all the model and data files you wish to use with your local agent. You can put more files into this directory at any time, but you must decide on the path of the directory before installing the agent. For example: `/Users/name/Documents/my-data-directory`.
- [Docker](https://docs.docker.com/engine/install/)
  - Agent deployment requires docker to have access to 8GB+ of memory. This can be set via Docker Desktop in Preferences > Resources > Advanced > Memory.
  - Include the absolute path of the directory containing the data and model files you intend to use with the local agent in Docker's File Sharing. This can be set via Docker Desktop in Preferences > Resources > File Sharing.
- [Helm](https://helm.sh/docs/intro/install/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)

The local agent can run on any K8s cluster. We recommend using Kind or Minikube for simplicity and easy mounting of your local files to the virtual nodes.

### Kind

1. Install [Kind](https://kind.sigs.k8s.io/docs/user/quick-start/#installation).
2. Create a configuration file for your Kind cluster that mounts the directory containing your data and models to `/ri-platform/local/` on the virtual nodes.
```yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
  extraMounts:
    - hostPath: <ABSOLUTE PATH ON LOCAL FILESYSTEM>
      containerPath: /ri-platform/local
```
3. With docker running, create the cluster: 
   1. `kind create cluster --config <above config file>`
4. Ensure your `kubectl` context is set to the cluster you created:
   1. `kubectl config use-context kind`
5. Follow the steps in [Deployment](deployment.md) to deploy an agent onto your Kind cluster.

### Minikube
1. Install [Minikube](https://minikube.sigs.k8s.io/docs/start/)
2. With docker running, create the cluster:
   - `minikube start`
3. Ensure your `kubectl` context is set to the cluster you created:
   - `kubectl config use-context minikube`
4. In a separate terminal, use a [9P mount](https://minikube.sigs.k8s.io/docs/handbook/mount/) to mount the directory containing your data and models to `/ri-platform/local` on the virtual nodes.
   - `minikube mount <ABSOLUTE PATH ON LOCAL FILESYSTEM>:/ri-platform/local`
   - This will create a long running process that must be kept alive in order for the mount to work properly.
5. Follow the steps in [Deployment](deployment.md) to deploy an agent onto your Minikube cluster.

## Using your Local Agent

When specifying paths to data or model files in test run configurations, replace the path to the directory on your local filesystem that you mounted with `/ri-platform/local`.

For example, if you mounted `/Users/name/Documents/my-data-directory`, and that directory contains:

- `data/`
  - `ref.csv`
  - `eval.csv`
- `model.py`

You would specify those files in a test configuration as:
```python
config = {
    "data_info": {
        "ref_path": "/ri-platform/local/data/ref.csv", 
        "eval_path": "/ri-platform/local/data/eval.csv",
        ...
    }, 
    "model_info": {
        "path": "/ri-platform/local/model.py"
    }, 
    ...
}

```

