# Configuration file for the Sphinx documentation builder.

project = "valopy"
copyright = "2025-present Vinc0739"
author = "Vinc0739"
release = "0.2.0"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_autodoc_typehints",
    "sphinx_rtd_dark_mode",
]

templates_path = ["_templates"]
exclude_patterns = []

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# Dark mode settings
default_dark_mode = True

# Enable search
html_search_language = "en"
