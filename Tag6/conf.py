# conf.py
import os
import sys
sys.path.insert(0, os.path.abspath('../'))

# -- Project information -----------------------------------------------------

project = 'MyProject'
copyright = '2023, MyName'
author = 'MyName'
version = '' # The short X.Y version
release = '' # The full version, including alpha/beta/rc tags

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',  # Support for Google style docstrings
    'sphinx.ext.napoleon',  # Support for NumPy and Google style docstrings
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

source_suffix = '.rst'
master_doc = 'index'
language = None

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'
html_static_path = ['_static']
