# CLI

The RI CLI can be run as follows:

```
rime-engine [COMMAND] [ARGUMENTS]
```

### Commands

For an up-to-date list of available commands, run `--help`:
```bash
rime-engine --help
```

The valid types of commands are:
- `create-firewall`: Create a firewall.
- `run-firewall`: Run firewall on a batch of tabular data.
- `run-firewall-images`: Run firewall on a batch of Image data.
- `run-firewall-nlp`: Run firewall on a batch of NLP data.
- `run-images`: Run RIME on image data
- `run-images-local`: Run RIME on image data and save to local file system
- `run-nlp`: Run RIME on NLP data
- `run-nlp-local`: Run RIME on NLP data and save to local file system
- `run-stress-tests`: Run RIME offline tests on tabular data
- `run-stress-tests-local`: Run RIME offline tests on tabular data and save to local file system
- `upload`: Upload Results

### Arguments

Different commands require different arguments.

The main arguments for most of these commands are:
- `--config-path`: Path to configuration
- `--upload-endpoint`: Endpoint to which results will be uploaded. [env var: `RIME_UPLOAD_URL`]
  - `--disable-tls` (optional): Whether to disable TLS encryption, which is enabled by default. Disabling TLS is recommended for local uploads. [env var: `RIME_DISABLE_TLS`]
- `--api-key`: The api key providing authentication to RI service. Required for external uploads. [env var: `RIME_API_KEY`]
- `--save-path` (optional): Path to save the results to. This will store the results locally as well as upload them to the specified endpoint
- `--run-name` (optional): Name of the Test Run. Overrides the Test Run Name in the configuration
- `--firewall-endpoint`: Endpoint for interacting with the firewall [env var: `RIME_FIREWALL_URL`]
- `--disable-firewall-events`: Disable processing events at a datapoint level when running firewall over a batch of data.

For an up-to-date list of available arguments for a given command, run `--help` with the command name:
```bash
rime-engine [COMMAND] --help
```

For stress testing only (`run-stress-tests`, `run-nlp`, and `run-images`):
- `--project-id` (optional): ID of the project the run should be added to

For firewall only (`run-firewall`, `run-firewall-nlp`, and `run-firewall-images`):
- `--firewall-id`: ID of the firewall testing instance the run should be added to
