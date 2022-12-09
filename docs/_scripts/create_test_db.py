import pandas as pd
from pathlib import Path
from rime.core.utils.deployment_utils import create_empty_tests
from rime.tabular.base.schema import ModelTask
from rime.tabular.data_tests.schema.config import DataTestSuiteConfig
from rime.core.run_tests import get_test_runners_and_configs
from rime.tabular.metric import ALL_METRICS
from rime.core.schema import TestCategory

all_run_modes = DataTestSuiteConfig.category_config_mapping().keys()
config = DataTestSuiteConfig(categories=list(all_run_modes) + [TestCategory.SUBSET_PERFORMANCE, TestCategory.SUBSET_PERFORMANCE_DRIFT])
metrics = [m() for m in ALL_METRICS]
runner_cls_and_configs = get_test_runners_and_configs(config, metrics)
runners = create_empty_tests(runner_cls_and_configs)
doc_path = Path('for_data_scientists/explanation/tests/')
type_to_type = {runner.type: runner._valid_tasks for runner in runners}
tests_dict = {}
for path in list(doc_path.rglob("*.md")):
    f = open(path)
    lines = f.readlines()
    cat = None
    name = None
    for l in lines:
        if l.startswith("## "):
            cat = l[3:-1]
        elif l.startswith("### "):
            name = l[4:-1]
            model_types = set()
            if path.parent.name in ("cv", "nlp"):
                model_types = {f"[{path.parent.name}] {path.name.split('_tests.md')[0]}"}
            else:
                runner = type_to_type[name]
                if runner is None:
                    model_types = {f"[tabular] {t}" for t in [v.value for v in ModelTask][:4]}
                else:
                    model_types ={f"[tabular] {t}" for t in runner}
        elif l.startswith("<p>"):
            desc = l.split('</p>')[0][3:]
            why_it_matters = l.split('<b>Why it matters:</b>')[1].split('</p>')[0][1:]
            if '<b>Configuration:</b>' in l:
                config = l.split('<b>Configuration:</b>')[1].split('</p>')[0][1:]
            else:
                config = None
            if name == "Nulls Per Feature Drift" and '[nlp] text_classification' in model_types:
                raise ValueError
            if name in tests_dict:
                if path.parent.name not in tests_dict[name]['modality']:
                    tests_dict[name]['modality'].append(path.parent.name)
                tests_dict[name]['model_types'].union(model_types)
            else:
                tests_dict[(name)] = {
                    'category': cat,
                    'desc': desc,
                    'why_it_matters': why_it_matters,
                    'modality': [path.parent.name],
                    "config": config,
                    'model_types': model_types
                }

pd.DataFrame([[k, v['category'], v['modality'], v['desc'], v['why_it_matters'], v['config'], list(v['model_types'])] for k,v in tests_dict.items()], columns=['name', 'category', 'modality', 'description', 'why_it_matters', 'config', 'model_types']).to_csv('test_db.csv', index=False)