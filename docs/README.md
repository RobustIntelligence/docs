# RIME Documentation
We use [Sphinx](https://www.sphinx-doc.org/en/master/index.html) to generate our documentation.

Individual articles are written in [markdown](https://www.sphinx-doc.org/en/master/usage/markdown.html) (`.md`), and navigational pages are written with [reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#) (`.rst`). Additionally, certain modules of Markedly Structured Text ([MySt](https://myst-parser.readthedocs.io/en/latest/index.html)) are used for such items as relative page references.

## Contribution Guidelines
Our documentation (and its structural ethos) is constantly in flux, but here are some starter guidelines:
- Keep it WYSIWYG (*"What You See is What You Get"*). The file structure of the docs should be very close to the structure presented in the built HTML, unless there is otherwise good reason.
- Keep it DRY (*"Don't Repeat Yourself"*) with [MyST substitutions](https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#substitutions-with-jinja2) (see bottom of `conf.py` for examples).
- Omit needless words (see [Strunk & White's Element's of Style #13](https://en.wikisource.org/wiki/The_Elements_of_Style/Principles)).
- When refactoring, check links often! `make linkcheck`

## To Build Locally
1. If not already created, go to the base of `rime` repo and create a virtualenv.
    - `python -m venv .venv && source .venv/bin/activate`
2. Install the dependencies to enable building.
    - `pip install -U pip && pip install -r docs/requirements.txt`
3. Return to the `docs/` module.
    - `cd docs`
4. (Optional) If you've changed page structure, refresh the build.
    - `make clean`
5. Build the html.
    - `make html`
6. Run the link checker.
    - `make linkcheck`
7. Open the local version.
    - `open build/html/index.html`

## To Release
We use [readthedocs](https://readthedocs.com/projects/robust-intelligence-inc-rime/) to publish our documentation online.
Certain branches are tracked and built automatically, each one creating its own "Version" of the documentation.

Generally, we keep one version called `latest` that tracks the `master/` branch and single versions
for each major release (e.g., branch `0.15-stable` is tracked to build version `0.15-stable`).

If you need to publish changes for a certain "Version", simply merge them into the appropriate branch
and they'll be built automatically.
