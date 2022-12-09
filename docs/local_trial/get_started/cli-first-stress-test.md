# Running Your First AI Stress Test

Let's begin by stress testing a binary classification model using the `rime-engine` CLI! This example uses a modified version of the <a href="https://www.kaggle.com/datasets/uciml/adult-census-income" target="_blank">Adult Census Income Dataset</a> from Kaggle that we've included in the `rime_trial/` bundle provided during installation.

Before beginning, make sure that you've completed [Installation](installation.md).

## Executing Stress Tests From the Command Line

Be sure to run this example from the `rime_trial/` directory so that local paths to datasets resolve correctly!

```bash
rime-engine run-stress-tests --config-path examples/income/stress_tests_model.json
```

{{ troubleshooting_python_package_redirect }}

## Analyzing Results in the Web Client

This command will run a batch of stress tests designed to detect vulnerabilities in your ML pipeline. The results will be uploaded to the "Default Project", which comes pre-seeded in your environment.

![](/_static/ui/ProjectsDefaultProject.png)

Once the command completes, you should be able to see the test run in the Default Project (see table below for URL).

![](/_static/ui/TestRunsIncomeExample.png)

From there, you can open the test run "Income (With Model)" and start exploring the results!

![](/_static/ui/TestsIncomeExample.png)

You can continue the rest of this example in [Validating Your Model with AI Stress Testing](../how_to_guides/rime_ai_stress_testing.md).
