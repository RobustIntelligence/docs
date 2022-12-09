# Download AI Stress Test Results

In some cases, you may want to cache the test results locally (e.g., if you need to restart the server and would like to preserve previous runs).

To do this, specify a `--save-path` when running stress testing:
```bash
rime-engine run-stress-tests --config-path <PATH-TO-CONFIGURATION> --save-path <SAVE-PATH>
```

This will cache results in a directory specified in `--save-path`. To directly re-upload the results, just do:

```bash
rime-engine upload --save-path <SAVE-PATH>
```
