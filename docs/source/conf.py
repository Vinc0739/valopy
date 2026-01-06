# Configuration file for the Sphinx documentation builder.
from importlib.metadata import version as get_version

project = "valopy"
copyright = "2025-present Vinc0739"
author = "Vinc0739"
release = "v" + get_version("valopy")

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx_autodoc_typehints",
    "sphinx_rtd_dark_mode",
]

templates_path = ["_templates"]
exclude_patterns = []

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]

# Dark mode settings
default_dark_mode = True

# Enable search
html_search_language = "en"

# Intersphinx configuration for linking to external documentation
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "aiohttp": ("https://docs.aiohttp.org/en/stable", None),
}
