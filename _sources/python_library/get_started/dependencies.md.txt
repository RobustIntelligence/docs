## Dependencies

Below are the python dependencies for the packages used in the RIME Python Library installation.

### RIME Python Package
`rime`
```
click
cryptography
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
opencv-python
pillow
requests
torch
torchvision
textstat
```

### RIME Trial Bundle
Used by sample data/models and the `rime_helper` utility (provided in the [trial bundle used during installation](installation.md)):
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
backcall==0.2.0
catboost==1.0.6
certifi==2022.6.15
cffi==1.15.0
charset-normalizer==2.1.0
click==8.1.3
cryptography==37.0.2
cycler==0.11.0
dataclasses-json==0.5.7
decorator==5.1.1
docker==5.0.3
fonttools==4.33.3
graphviz==0.20
grpcio==1.44.0
grpcio-health-checking==1.34.1
grpcio-reflection==1.34.1
grpcio-tools==1.44.0
idna==3.3
importlib-metadata==4.12.0
ipython==7.34.0
jedi==0.18.1
joblib==1.1.0
kiwisolver==1.4.3
llvmlite==0.38.1
marshmallow==3.17.0
marshmallow-enum==1.5.1
matplotlib==3.5.2
matplotlib-inline==0.1.3
mypy-extensions==0.4.3
mypy-protobuf==3.0.0
nlpaug==1.1.8
numba==0.55.2
numpy==1.21.6
opencv-python==4.6.0.66
packaging==21.3
pandas==1.3.5
parso==0.8.3
pexpect==4.8.0
pickleshare==0.7.5
Pillow==9.1.1
plotly==5.9.0
portalocker==2.0.0
prompt-toolkit==3.0.30
protobuf==3.20.1
ptyprocess==0.7.0
pycparser==2.21
Pygments==2.12.0
PyJWT==2.4.0
pyparsing==3.0.9
pyphen==0.12.0
python-dateutil==2.8.2
python-dotenv==0.20.0
pytz==2022.1
PyYAML==6.0
requests==2.28.1
rime==0.17.0rc9
sacrebleu==1.5.1
scikit-learn==1.0.2
scipy==1.7.3
simplejson==3.17.6
six==1.16.0
tenacity==8.0.1
textstat==0.7.3
threadpoolctl==3.1.0
torch==1.12.0
torchvision==0.13.0
tqdm==4.64.0
traitlets==5.3.0
types-protobuf==3.19.22
typing-inspect==0.7.1
typing_extensions==4.2.0
urllib3==1.26.9
validators==0.20.0
wcwidth==0.2.5
websocket-client==1.3.3
zipp==3.8.0
```
