# -- Path setup ----------------------------------------
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -------------------------------
project = 'Medium Multiply'
copyright = '2020, Joffrey Bienvenu'
author = 'Joffrey Bienvenu'

# -- General configuration -----------------------------
extensions = [
    'recommonmark',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output ---------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
