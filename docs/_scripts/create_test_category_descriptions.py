"""Write descriptions for all RIME test categories."""
import logging
from pathlib import Path
EXPLANATION_DIR = Path(Path(__file__).parents[1].absolute(),  "for_data_scientists", "explanation")

from rime.tabular.data_tests.schema.config import DataTestSuiteConfig
from rime.nlp.model_tests.schema.test_suite import ClassificationTestSuiteConfig

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def tabular_main():
    """Generate tabular test categories and output to file."""
    output_file = EXPLANATION_DIR / "tabular_test_categories.md"
    EXPLANATION_DIR.mkdir(exist_ok=True, parents=True)
    all_strings = ["# Summary Tests\n"]
    config = DataTestSuiteConfig()
    for category_test in config.category_test_map.values():
        all_strings.append(f"## {category_test.name}\n")
        clean_description = category_test.description.replace("\n", "").strip(" ")
        all_strings.append(clean_description)
        all_strings.append("\n")
    with output_file.open("w") as f:
        f.writelines(all_strings)


def unstructured_main():
    """Generate unstructured test categories and output to file."""
    output_file = EXPLANATION_DIR / "unstructured_test_categories.md"
    EXPLANATION_DIR.mkdir(exist_ok=True, parents=True)
    all_strings = ["# Summary Tests\n"]
    config = ClassificationTestSuiteConfig()
    for category_test in config.category_test_map.values():
        all_strings.append(f"## {category_test.name}\n")
        clean_description = category_test.description.replace("\n", "").strip(" ")
        all_strings.append(clean_description)
        all_strings.append("\n")
    with output_file.open("w") as f:
        f.writelines(all_strings)


if __name__ == "__main__":
    tabular_main()
    unstructured_main()
