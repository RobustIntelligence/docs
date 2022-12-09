<style>
#warning-box {
  font-size:16px;
  padding:15px;
  margin-bottom:27px;
  border:1px solid transparent;
  border-radius:4px;
  background-color:#f2dede;
  border-color:#ebccd1;
}

#alert-yellow {
  font-size:16px;
  padding:15px;
  margin-bottom:27px;
  border:1px solid transparent;
  border-radius:4px;
  background-color:#fcf8e3;
  border-color:#faebcc;
}

#alert-blue {
  font-size:16px;
  padding:15px;
  margin-bottom:27px;
  border:1px solid transparent;
  border-radius:4px;
  background-color:#e3e7fc;
  border-color:#cddcfa;
}

#alert-turquoise {
  font-size:16px;
  padding:15px;
  margin-bottom:27px;
  border:1px solid transparent;
  border-radius:4px;
  background-color:#e3f4fc;
  border-color:#ccf2fa;
}

#turquoise-header {
  font-size:16px;
  padding:15px;
  margin-bottom:27px;
  border:1px solid transparent;
  border-radius:4px;
  border-color:#3b808a;
  color:#3b808a;
}

#yellow-header {
  font-size:16px;
  padding:15px;
  margin-bottom:27px;
  border:1px solid transparent;
  border-radius:4px;
  border-color:#8a6d3b;
  color:#8a6d3b;
}

#blue-header {
  font-size:16px;
  padding:15px;
  margin-bottom:27px;
  border:1px solid transparent;
  border-radius:4px;
  border-color:#3B588A;
  color:#3B588A;
}
</style>

# Installation

## Pre-requisites
Before beginning, please ensure you have the following:
- The following system requirements:
    - 3.7 ≤ `python` ≤ 3.9
    - one of the following package managers
        - `pip`
        - `conda`
- The `rime_trial` bundle ( {{ '[download here](https://storage.googleapis.com/rime-trial-zips/rime-trial-{}.tar.gz)'.format(env.config.version) }} )
- A `token.txt` file (will be provided by your RI representative)

## Set Up Your Environment
To avoid interfering with your other projects' dependencies, we will create a new Python virtual environment for RIME.

1. Download ( {{'[link here](https://storage.googleapis.com/rime-trial-zips/rime-trial-{}.tar.gz)'.format(env.config.version)}} )
   and extract ({{ '`tar -xzf rime-trial-{}.tar.gz`'.format(env.config.version) }}) the `rime_trial` bundle.
2. Place the `token.txt` file inside of `rime_trial/`.
3. Step into `rime_trial/` --- this will be our working directory throughout the installation.
4. Select a virtual environment manager (currently either `pip` or Conda) and follow the appropriate instructions below.
    <p id="alert-turquoise">
    <b>Pip Installation</b>
    </p>

    1. Create a new [python virtual
    environment](https://docs.python.org/3/library/venv.html).
        ```
        python -m venv rime-venv
        ```
    2. Activate the virtual environment.
       <p id="turquoise-header">
       <b>macOS & Linux</b>
       </p>

       ```bash
       source rime-venv/bin/activate
       ```

       <p id="blue-header">
       <b>Windows</b>
       </p>

       ```powershell
       .\rime-venv\Scripts\activate
       ```
    3. Update pip and install required Python packages from
        `trial_requirements.txt`.
        ```
        pip install --upgrade pip
        pip install -r trial_requirements.txt
        ```

    <p id="alert-blue">
    <b>Conda Installation</b>
    </p>

    1. Create a new [conda virtual
    environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).
    Replace `$PYTHON_VERSION_YOU_WISH_TO_USE` with the version of Python that you
    wish to use (e.g., `3.8`).
        ```
        conda create --name rime-venv python=$PYTHON_VERSION_YOU_WISH_TO_USE
        ```
    2. Activate the virtual environment.
        ```
        conda activate rime-venv
        ```
    5. Update pip and install required Python packages from
        `trial_requirements.txt`.
        ```
        pip install --upgrade pip
        pip install -r trial_requirements.txt
        ```

## Generate Requirements Files and Install
1. Generate the requirements files.
    ```bash
    python rime_helper.py generate-rime-requirements
    ```
2. Register your product license.
    ```bash
    python rime_helper.py update-license
    ```
3. Install the RIME Python package.
    ```bash
    pip install -r rime_requirements.txt
    ```

### Install the RIME NLP Dependencies (Optional)
To use RIME for stress testing NLP models, additional Python dependencies must be installed.

```bash
pip install -r nlp_requirements.txt
```

### Install the RIME CV Dependencies (Optional)
To use RIME for stress testing Computer Vision models, additional Python dependencies must be installed.

```bash
pip install -r cv_requirements.txt
```

