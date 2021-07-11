# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import sphinx_material

# -- Project information -----------------------------------------------------

project = 'galileo tutorials'
copyright = '2021, Hypernet Labs'
author = 'Hypernet Labs'

autodoc_default_flags = ['members']
autosummary_generate = True
autosummary_imported_members = True

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [ 'myst_parser', 'sphinx.ext.autosummary', "sphinx.ext.autodoc" ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_material'
# Get the them path
html_theme_path = sphinx_material.html_theme_path()
# Register the required helpers for the html context
html_context = sphinx_material.get_html_context()

html_theme_options = {
    "repo_name": "Galileo-Tutorial-Pages",
    "repo_url": "https://github.com/GoHypernet/Galileo-Tutorial-Pages",
    "html_minify": True,
    "css_minify": True,
    "nav_title": "Galileo Tutorials",
    "globaltoc_depth": 3,
    "theme_color": "#4dc1ab",
    "color_primary": "teal",
    "globaltoc_collapse": True,
    "globaltoc_includehidden": True,
    "version_dropdown": False,
}

master_doc = "index"

html_sidebars = {"**": ["globaltoc.html"]}

html_logo = "./docs/images/galileo-logo.png"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']