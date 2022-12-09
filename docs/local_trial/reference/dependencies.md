## Dependencies

Below are the python dependencies for the packages used in the Local Trial installation.

### Python Package
`rime`
```
click
cryptography
databricks-sql-connector
dataclasses-json>=0.3.7
grpcio==1.44.0
grpcio-health-checking==1.34.1
grpcio-reflection==1.34.1
grpcio-tools==1.44.0
IPython
joblib
mypy-protobuf==3.0
numba
numpy
pandas>=1.1.0
pyjwt
python-dateutil
scikit-learn
scipy>=1.5.0
simplejson
tqdm
validators
```

### Additional NLP Dependencies
`rime[nlp]`
```
anyascii
sacrebleu==1.5.1
nlpaug<=1.1.8
nltk>=3.4.5
requests
torch
textstat
```

### Additional CV Dependencies
`rime[images]`
```
anyascii
sacrebleu==1.5.1
nlpaug<=1.1.8
nltk>=3.4.5
opencv-python
pillow
requests
torch
torchvision
textstat
```

### Trial Bundle
Used by sample data/models and the `rime_helper` utility (provided in the [trial bundle used during installation](/local_trial/get_started/installation.md)):
```
catboost
docker
python-dotenv
wheel
pyyaml
```

### Full List of Dependencies
NOTE: the full list of dependencies was generated using the `pip freeze` command, so the versions here are the default used by pip at the time of the latest release and are not strict requirements.

```
anyascii==0.3.1
appnope==0.1.3
asttokens==2.0.8
backcall==0.2.0
certifi==2022.6.15
cffi==1.15.1
charset-normalizer==2.1.0
click==8.1.3
cryptography==37.0.4
databricks-sql-connector==2.0.4
dataclasses-json==0.5.7
decorator==5.1.1
executing==0.10.0
grpcio==1.44.0
grpcio-health-checking==1.34.1
grpcio-reflection==1.34.1
grpcio-tools==1.44.0
idna==3.3
ipython==8.4.0
jedi==0.18.1
joblib==1.1.0
llvmlite==0.39.0
marshmallow==3.17.0
marshmallow-enum==1.5.1
matplotlib-inline==0.1.6
mypy-extensions==0.4.3
mypy-protobuf==3.0.0
nlpaug==1.1.8
nltk==3.7
numba==0.56.0
numpy==1.22.4
packaging==21.3
pandas==1.4.3
parso==0.8.3
pexpect==4.8.0
pickleshare==0.7.5
portalocker==2.0.0
prompt-toolkit==3.0.30
protobuf==3.20.1
ptyprocess==0.7.0
pure-eval==0.2.2
pyarrow==9.0.0
pycparser==2.21
Pygments==2.13.0
PyJWT==2.4.0
pyparsing==3.0.9
pyphen==0.12.0
python-dateutil==2.8.2
pytz==2022.2.1
regex==2022.8.17
requests==2.28.1
sacrebleu==1.5.1
scikit-learn==1.1.2
scipy==1.9.0
simplejson==3.17.6
six==1.16.0
stack-data==0.4.0
textstat==0.7.3
threadpoolctl==3.1.0
thrift==0.13.0
torch==1.12.1
tqdm==4.64.0
traitlets==5.3.0
types-protobuf==3.19.22
typing-inspect==0.8.0
typing_extensions==4.3.0
urllib3==1.26.11
validators==0.20.0
wcwidth==0.2.5
```
