# Debugging the Python Package

1. **I'm seeing "Missing option" errors with my `rime-engine` CLI commands! How do I resolve them?**

    ```
    rime-engine run-stress-tests --config-path examples/income/stress_tests_model.json

    Error: Missing option '--upload-endpoint'.

    ..
    ```

    The commands in the `rime-engine` CLI [How-To Guides](/local_trial/how_to_guides.rst) use **environment variables** to keep the commands short and readable.

    Be sure to set these up in your terminal session before running any commands:

    **Local**

    NOTE: Disabling TLS is recommended *for local uploads only*!

    ```
    export RIME_UPLOAD_URL=localhost:5001
    export RIME_FIREWALL_URL=localhost:5002
    export RIME_DISABLE_TLS=True
    ```

    **Managed Cloud**

    Be sure to replace ``<YOUR_ORG_NAME>`` and ``<YOUR_API_KEY`` with the specific values for your RI Managed Cloud instance!

    ```
    export RIME_UPLOAD_URL=rime.<YOUR_ORG_NAME>.rime.dev
    export RIME_FIREWALL_URL=rime.<YOUR_ORG_NAME>.rime.dev
    export RIME_API_KEY=<YOUR_API_KEY>
    ```

    Alternatively, missing options can be provided in the command itself, as flags (e.g., `--upload-endpoint` below):
    ```
    rime-engine run-stress-tests --config-path examples/income/stress_tests_model.json --upload-endpoint <YOUR_UPLOAD_ENDPOINT>
    ```

    Mappings of environment variables to their option names can be found by running `--help` for the chosen command:
    ```
    rime-engine run-stress-tests --help
    ```

2. **I'm seeing `ModuleNotFound` errors in the console. How do I resolve them?**

    These errors likely result from not having the extras installed for your use case.

    Make sure you are inside of the `rime_trial/` directory using your `rime-venv` virtual environment before proceeding.

    (If not already run during installation) Run the following to generate the necessary requirements lists:
    ```bash
    python rime_helper.py generate-rime-requirements --token-file $PATH_TO_TOKEN_TXT_FILE
    ```

    For Natural Language Processing (NLP) use cases (i.e., text data):
    ```bash
    pip install -r nlp_requirements.txt
    ```

    For Computer Vision (CV) use cases (i.e., image data):
    ```bash
    pip install -r cv_requirements.txt
    ```

3. **I'm seeing `grpc.FutureTimeoutError`(s) when trying to upload stress tests. How do I resolve them?**

    This error can be due to DNS resolution across operating systems and protocols (IPv4 vs. IPv6).

    If that is the case, running the following in your terminal session can resolve the issue:
    ```bash
    export GRPC_DNS_RESOLVER=native
    ```

    Otherwise, make sure your machine has access to the endpoint(s) in question (e.g., by enabling VPN).
