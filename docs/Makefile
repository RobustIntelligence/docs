# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = build
RELEASE_VERSION_FILE := ../version.txt
RELEASE_VERSION ?= $(shell cat ${RELEASE_VERSION_FILE})

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help clean Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
html:
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" -D version="$(RELEASE_VERSION)" $(SPHINXOPTS) $(0)

linkcheck: html
	linkchecker --check-extern --ignore-url="localhost.*|storage.googleapis.com/rime-trial-zips/.*"  "$(BUILDDIR)"/html/index.html

latexpdf:
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" -D version="$(RELEASE_VERSION)" $(SPHINXOPTS) $(0)

latex:
	@pandoc --toc --latex-engine=pdflatex -V fontfamily="cmbright" -V geometry=margin=0.5in -V documentclass="book" -o /build/<output>.pdf -s <input_1>.md <input_N>.md <copyright>.md


clean:
	rm -rf "$(BUILDDIR)"
