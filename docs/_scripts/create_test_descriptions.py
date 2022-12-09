"""Write descriptions for all RIME test suites."""
import logging
from pathlib import Path
from typing import List

from rime.images.schema.task import Task as ImageTask
from rime.nlp.schema.task import Task
from rime.images.deployment_utils import get_test_suite_description_strings as get_cv_descriptions
from rime.nlp.utils.deployment_utils import (
    get_test_suite_description_strings as get_nlp_descriptions,
)
from rime.tabular.deployment_utils import (
    get_test_suite_description_strings as get_tabular_descriptions,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TEST_BANK_DIR = Path(Path(__file__).parents[1].absolute(),  "for_data_scientists", "explanation", "tests")

def get_task_filename(task: Task):
    """Convert task display name to file name."""
    task_name: str = task.value
    task_name_formatted = task_name.lower().replace(" ", "_")
    return f"{task_name_formatted}_tests.md"


def generate_file(all_strings: List[str], file_path: Path):
    """Output file with task-specific test descriptions."""
    with file_path.open("w") as f:
        f.writelines(all_strings)


def tabular_main():
    """Generate Tabular test suite descriptions and output to file."""
    output_dir = TEST_BANK_DIR / "tabular"
    output_dir.mkdir(exist_ok=True, parents=True)
    descriptions = get_tabular_descriptions()
    descriptions[0] = f"# Tests\n"
    filename = "tests.md"
    file_path = output_dir / filename
    generate_file(descriptions, file_path)
    logger.info(f"Wrote tabular Test Suite descriptions to {file_path}")


def update_header(description_list: List[str], task: Task) -> None:
    """Update the tests header."""
    description_list[0] = f"# {task.value} Tests\n"


def nlp_main():
    """Generate NLP test suite descriptions and output to file."""
    output_dir = TEST_BANK_DIR / "nlp"
    output_dir.mkdir(exist_ok=True, parents=True)
    # TODO: Add other tasks.
    tasks = [Task.CLASSIFICATION, Task.NER, Task.NLI]
    for task in tasks:
        task_descriptions = get_nlp_descriptions(task)
        update_header(task_descriptions, task)
        filename = get_task_filename(task)
        file_path = output_dir / filename
        generate_file(task_descriptions, file_path)
        logger.info(
            f'Wrote NLP task "{task.value}" test suite descriptions to {output_dir / filename}'
        )


def cv_main():
    """Generate CV test suite descriptions and output to file."""
    output_dir = TEST_BANK_DIR / "cv"
    output_dir.mkdir(exist_ok=True, parents=True)
    tasks = [ImageTask.CLASSIFICATION, ImageTask.OBJECT_DETECTION]
    for task in tasks:
        task_descriptions = get_cv_descriptions(task)
        update_header(task_descriptions, task)
        filename = get_task_filename(task)
        file_path = output_dir / filename
        generate_file(task_descriptions, file_path)
        logger.info(
            f'Wrote CV task "{task.value}" test suite descriptions to {output_dir / filename}'
        )


if __name__ == "__main__":
    tabular_main()
    nlp_main()
    cv_main()
