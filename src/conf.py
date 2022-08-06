# -*- coding: utf-8 -*-
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


import sphinx_rtd_theme
from datetime import date


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Mike Mabey"
copyright = "2015-%s, Mike Mabey" % date.today().strftime("%Y")
author = "Mike Mabey"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_rtd_theme",
    # 'sphinx_markdown_tables',
    "myst_parser",
    "ablog",
    "sphinx.ext.intersphinx",
]

templates_path = ["_templates"]
exclude_patterns = ["blog/sample_blog.md", "blog/drafts"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = "Mike Mabey"
html_favicon = "_static/favicon.ico"
html_static_path = ["_static"]
html_extra_path = ["other/"]
html_last_updated_fmt = "%B %d, %Y"
html_copy_source = False

html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "collapse_navigation": False,
    "display_version": False,
}
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_css_files = ["custom.css"]

# ABlog options
blog_post_pattern = [f"blog/*/*/*.{ext}" for ext in ("rst", "md")]


# --------- Original starts here $$$$$$$$$$$$$$$
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))

# The suffix of source filenames.
source_suffix = [".rst", ".md"]
# source_parsers = {
#     ".md": "recommonmark.parser.CommonMarkParser",
# }

# The encoding of source files.
source_encoding = "utf-8"

# The master toctree document.
master_doc = "index"

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# -- Options for HTML output ----------------------------------------------

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
html_use_opensearch = "http://mikemabey.com"

# Output file base name for HTML help builder.
htmlhelp_basename = "MyWebsitedoc"
