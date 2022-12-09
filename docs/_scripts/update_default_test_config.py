"""Create default test config."""
import json
import re
from pathlib import Path
from typing import Type

from rime.core.cli.output_schema import TestingType
from rime.core.metric import Metric
from rime.core.test_suite_config import TestSuiteConfig
from rime.images.schema.test_suite import (
    ClassificationTestSuiteConfig as ImageClassificationTestSuiteConfig,
)
from rime.nlp.model_tests.schema.test_suite import (
    ClassificationTestSuiteConfig,
    NERDModelTestSuiteConfig,
)
from rime.tabular.data_tests.schema.config import DataTestSuiteConfig


def dump_config(path: Path, config_cls: Type[TestSuiteConfig]) -> None:
    """Write default config to disk."""
    s = path.open("r").read()
    pattern = re.compile("```(python|json)\n[^`]*```")
    match = pattern.search(s)
    config = config_cls.from_config_dict({}, TestingType.STRESS)
    config_dict = config.to_dict()
    if "testing_type" in config_dict:
        del config_dict["testing_type"]
    for test_config in config_dict.values():
        if isinstance(test_config, dict) and isinstance(
            test_config.get("metric", None), Metric
        ):
            del test_config["metric"]  # cannot json encode objects
    config_s = json.dumps(config_dict, indent=2)
    formatted_s = f"```{match.groups()[0]}\n{config_s}\n```"
    updated_doc = s[: match.start()] + formatted_s + s[match.end() :]
    with path.open("w") as f:
        f.write(updated_doc.strip())


if __name__ == "__main__":
    file_name = "tests.md"
    top_level_dir = Path(__file__).parents[1].absolute()
    parent_dir = Path(top_level_dir, "for_data_scientists", "reference")
    # Tabular
    directory = parent_dir / "tabular"
    dump_config(directory / file_name, DataTestSuiteConfig)

    # NLP
    directory = parent_dir / "nlp" / "tasks_test_suite"
    config_map = {
        directory / "named_entity_recognition.md": NERDModelTestSuiteConfig,
        directory / "text_classification.md": ClassificationTestSuiteConfig,
        directory / "natural_language_inference.md": ClassificationTestSuiteConfig,
    }

    for path, config_class in config_map.items():
        dump_config(path, config_class)

    # Images
    directory = parent_dir / "cv" / "tasks_test_suite"
    config_map = {
        directory / "image_classification.md": ImageClassificationTestSuiteConfig
    }

    for path, config_class in config_map.items():
        dump_config(path, config_class)
