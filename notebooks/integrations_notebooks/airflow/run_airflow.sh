#!/bin/bash

CURR_BASH_SCRIPT_PID=$(echo $$)
# Get the directory of the script
AIRFLOW_SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cleanup() {
    # Kill this script process and its children (cleans up all related processes cleanly)
    pkill -9 -P $CURR_BASH_SCRIPT_PID || true
}

# This part ensures the cleanup function defined above gets called at the end
for sig in INT QUIT HUP TERM ALRM USR1; do
    trap "
    trap - $sig EXIT
    kill -s $sig "'"$$"' "$sig"
done
trap 'cleanup' EXIT

# Check python version is greater than or equal to 3.8
# Otherwise, the Scikit-learn version of OHEncoder will not work properly
PYTHON_MINOR_VERSION=$(python3 -c 'import sys; print(sys.version_info[1])')
if [ "$PYTHON_MINOR_VERSION" -lt "8" ]; then
    echo "Python version 3.8 or higher is required to run this demo. Exiting."
    exit 1
fi
if [[ -z "${RIME_UPLOAD_URL}" ]]; then
    echo "Environment variable \$RIME_UPLOAD_URL is not set."
    echo "Please specify the cluster URL (e.g., " \
         "'export RIME_UPLOAD_URL=rime.<cluster-name>.rime.dev')"
    exit 1
elif [[ -z "${RIME_API_KEY}" ]]; then
    echo "Environment variable $RIME_API_KEY is not set."
    echo "Please specify your valid API key for the target RIME cluster." \
        " (e.g., 'export RIME_API_KEY=abcd1234567890')"
    exit 1
fi


# Create a virtual environment for the demo dependencies
python3 -m pip install --upgrade pip
python3 -m pip install virtualenv
python3 -m virtualenv -p python3 $AIRFLOW_SCRIPT_DIR/.venv-airflow
# Activate the virtual environment
source $AIRFLOW_SCRIPT_DIR/.venv-airflow/bin/activate

# Airflow needs a home. `~/airflow` is the default, but you can put it
# somewhere else if you prefer (optional)
export AIRFLOW_HOME=~/airflow

# See: https://github.com/apache/airflow/issues/16573
# Stress test runs are occasionally prematurely terminated by airflow
# if we use the default of 30s.
export AIRFLOW__SCHEDULER__ORPHANED_TASKS_CHECK_INTERVAL=300.0

# See https://airflow.apache.org/blog/airflow-1.10.10/#running-airflow-on-macos
# This helps avoid segfaults when running on MacOS
export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES

# Permit pickling to facilitate easier cross-task communication
# As always, pickling is a security risk if you do not trust your
# environment. But we are doing everying in a dev/standalone setup.
export AIRFLOW__CORE__ENABLE_XCOM_PICKLING=True

# Set the base_url of the webserver to be 8081 to avoid
# conflicts with RIME's web server port
AIRFLOW_PORT=8081
export AIRFLOW__CLI__ENDOINT_URL=$AIRFLOW_PORT
export AIRFLOW__WEBSERVER__BASE_URL="http://localhost:${AIRFLOW_PORT}"
export AIRFLOW__WEBSERVER__WEB_SERVER_PORT=$AIRFLOW_PORT

MLFLOW_PORT=7081
export MLFLOW_TRACKING_URI="http://0.0.0.0:${MLFLOW_PORT}"
mkdir -p $AIRFLOW_HOME/dags

# Now copy the DAG file to the default location
cp $AIRFLOW_SCRIPT_DIR/airflow_demo.py $AIRFLOW_HOME/dags

# Install Airflow using the constraints file
AIRFLOW_VERSION=2.3.2
PYTHON_VERSION="$(python3 --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
# For example: 3.7
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
# For example: https://raw.githubusercontent.com/apache/airflow/constraints-2.3.2/constraints-3.7.txt
python3 -m pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
python3 -m pip install --no-cache mlflow joblib catboost scikit-learn
python3 -m pip install rime-sdk

# Download the example data.
python3 -m pip install https://github.com/RobustIntelligence/ri-public-examples/archive/master.zip
echo "Downloading Example Fraud Data"
python3 -c "from ri_public_examples.download_files import download_files; download_files('tabular/fraud', '${AIRFLOW_HOME}/fraud_data')"

# Setup mlflow tracking server
pushd $AIRFLOW_HOME
mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./artifacts --host 0.0.0.0 --port $MLFLOW_PORT &
popd

# The Standalone command will initialise the database, make a user,
# and start all components for you.
airflow standalone

# Visit localhost:8081 in the browser and use the admin account details
# shown on the terminal to login.
# Enable the Airflow_RIME_Demo dag in the home page to get started
# Visit http://localhost:7081/ to see the MLflow UI.
deactivate
