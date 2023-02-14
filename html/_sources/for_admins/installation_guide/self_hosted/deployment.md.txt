# Deploying Your RI Platform Cluster

With requirements satisfied and configuration files populated, you are now ready to deploy the RI Platform.

At a high-level, there are two main ways to do this: as a standalone Kubernetes cluster (recommended) or integrated within an existing Kubernetes cluster. The former is achieved by specifying `create_eks = true`, whereas the latter is specified by `create_eks = false` and including a `cluster_name`.

The steps below may vary, depending on your infrastructure.

## Deploy the Cluster

1. Open a terminal session on a box containing the installation tools.
2. Verify that your Terraform configuration files (`main.tf` and `backend.tf`) are present in your working directory.
3. Authenticate your AWS CLI.
   ```shell
   aws sts get-caller-identity # verify you're in the right account
   ```
4. Add the Robust Intelligence Helm repository (or your private registry, if configured).
   ```shell
   helm repo add robustintelligence https://robustintelligence.github.io/helm --force-update
   ```
5. Initialize your Terraform environment.
   ```shell
   terraform init
   ```
6. Verify your Terraform plan (recommended).
   ```shell
   terraform plan -out "rime.plan" | tee "rime-plan.txt"
   less rime-plan.txt # proof-read the changes
   ```
7. **Terraform apply!** (This step can take up to ~30 minutes.)
   ```shell
   terraform apply "rime.plan" # if you skipped #6, you can omit the "rime.plan"
   ```

---

## Validate Your Deployment

Once the `terraform apply` command completes, your cluster should be operational! The following actions can help verify all services are up and running.

### Load Balancer ALPN Policy

1. Find the load balancer used by the `rime-kong-proxy` with `kubectl get svc rime-kong-proxy`.
2. Locate the Load Balancer in your AWS console.
3. In the "Listeners" section, verify that the `TLS: 443` listener's ALPN policy is set to `HTTP2Preferred`.

### Kubernetes Services

1. Point your local `kubectl` to the new cluster.
   ```shell
   aws eks --region us-west-2 update-kubeconfig --name <cluster-name>
   ```
2. Inspect the running pods.
   ```shell
   kubectl get pods -n <rime-namespace>
   ```
   Your output should look something like this:
   ```
   NAME                                             READY   STATUS      RESTARTS   AGE
   rime-agent-job-monitor-6bddd4697d-t9118          1/1     Running     0          5m26s
   rime-agent-launcher-56bc47549c-dod60             1/1     Running     0          5m26s
   rime-frontend-cd6c89884-8ljrl                    1/1     Running     0          5m26s
   ...
   ```
2. Verify you can access the web client at your `rime` sub-domain. This domain is the value you configured during DNS setup and will be of the form (`rime.<DOMAIN>.com`).
3. cURL your version endpoint and verify that metadata is successfully returned:
   ```shell
   curl --location --request GET rime.<DOMAIN>.com/v1/version
   ```
4. Verify you can make an API token in the web client using this [guide](/for_admins/how_to_guides/api-authentication.md).
5. Test your Python SDK connection using the API token you made:
   ```shell
   pip install rime-sdk
   ```

   ```python
   rime_client = Client("rime.<DOMAIN>.com", "<API_TOKEN>")
   project = rime_client.create_project("Health Check", "Testing the SDK's upstream connection.")
   ```
5. Return to the web client and verify that a project was created. If everything succeeds you are ready to achieve ML Integrity with the RI Platform!

## Configure Backups

Backups ensure that your team can restore your testing data in the event of a disaster.
If your cluster has been successfully deployed (and you opted in via `install_velero = true`), you can configure backups using the steps below.

1. Download Velero.
   ```shell
   curl -fsSL -o velero-v1.6.3-linux-amd64.tar.gz https://github.com/vmware-tanzu/velero/releases/download/v1.6.3/velero-v1.6.3-linux-amd64.tar.gz
   tar -xvf velero-v1.6.3-linux-amd64.tar.gz
   ```
2. Ensure that your backups are scheduled properly.
   ```shell
   ./velero schedule get -n rime-extras
   ```

---

## Troubleshooting

1. If you are getting timeouts in the SDK, ensure that you are connected to VPN.
2. If the webapp is marked as insecure, verify that you have an ACM SSL/TLS cert for your webapp.
3. On older operating systems, you may need to run `export GRPC_DNS_RESOLVER=native` in the shell. Otherwise requests may hang due to ipv4 vs ipv6 issues.

