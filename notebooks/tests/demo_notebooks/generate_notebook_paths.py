import os
import json

def generate_notebook_paths():
  notebooks = os.popen("cd docs/notebooks/demo_notebooks && find . -name \"*.ipynb\" | awk '{ result = (NR > 1 ? result \", \" : \"\") $1 } END { print result}'").read().strip()
  notebooks_json = json.dumps([nb.strip() for nb in notebooks.split(",")])
  # We need to call print here because the notebooks_json is captured by github from STDOUT
  print(notebooks_json)

if __name__ == "__main__":
  generate_notebook_paths()
