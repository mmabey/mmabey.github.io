#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Mike Mabey build configuration file, created by
# `ablog start` on Sat Sep 17 06:58:45 2022.
#
# Note that not all possible configuration values are present in this file.
# All configuration values have a default; values that are commented out
# serve to show the default.

from datetime import date

import ablog
import sphinx_rtd_theme

# -- General ABlog Options ----------------------------------------------------

# A path relative to the configuration directory for blog archive pages.
blog_path = "posts"

# The "title" for the blog, used in active pages.  Default is ``'Blog'``.
blog_title = "Mike Mabey's Blog"

# Base URL for the website, required for generating feeds.
# e.g. blog_baseurl = "http://example.com/"
blog_baseurl = "https://blog.mikemabey.com"

# Choose to archive only post titles. Archiving only titles can speed
# up project building.
# blog_archive_titles = False

# -- Blog Authors, Languages, and Locations -----------------------------------

# A dictionary of author names mapping to author full display names and
# links. Dictionary keys are what should be used in ``post`` directive
# to refer to the author.  Default is ``{}``.
blog_authors = {
    "Mike Mabey": ("Mike Mabey", None),
}


# A dictionary of language code names mapping to full display names and
# links of these languages. Similar to :confval:`blog_authors`, dictionary
# keys should be used in ``post`` directive to refer to the locations.
# Default is ``{}``.
# blog_languages = {
#    'en': ('English', None),
# }


# A dictionary of location names mapping to full display names and
# links of these locations. Similar to :confval:`blog_authors`, dictionary
# keys should be used in ``post`` directive to refer to the locations.
# Default is ``{}``.
# blog_locations = {
#    'Earth': ('The Blue Planet', 'https://en.wikipedia.org/wiki/Earth),
# }

# -- Blog Post Related --------------------------------------------------------

# Format date for a post.
post_date_format = "%b %d, %Y"
post_date_format_short = "%Y %b %d"

# Number of paragraphs (default is ``1``) that will be displayed as an excerpt
# from the post. Setting this ``0`` will result in displaying no post excerpt
# in archive pages.  This option can be set on a per post basis using
# post_auto_excerpt = 1

# Index of the image that will be displayed in the excerpt of the post.
# Default is ``0``, meaning no image.  Setting this to ``1`` will include
# the first image, when available, to the excerpt.  This option can be set
# on a per post basis using :rst:dir:`post` directive option ``image``.
# post_auto_image = 0

# Number of seconds (default is ``5``) that a redirect page waits before
# refreshing the page to redirect to the post.
# post_redirect_refresh = 5

# When ``True``, post title and excerpt is always taken from the section that
# contains the :rst:dir:`post` directive, instead of the document. This is the
# behavior when :rst:dir:`post` is used multiple times in a document. Default
# is ``False``.
# post_always_section = False

# When ``True``, links to the previous and next posts will be rendered at the
# bottom of the page.
# Default is ``True``
post_show_prev_next = False

# When ``False``, the :rst:dir:`orphan` directive is not automatically set
# for each post. Without this directive, Sphinx will warn about posts that
# are not explicitly referenced via another document. :rst:dir:`orphan` can
# be set on a per-post basis as well if this is false. Default is ``True``.
# post_auto_orphan = True

# -- ABlog Sidebars -------------------------------------------------------

# There are seven sidebars you can include in your HTML output.
# postcard.html provides information regarding the current post.
# recentposts.html lists most recent five posts. Others provide
# a link to a archive pages generated for each tag, category, and year.
# In addition, there are authors.html, languages.html, and locations.html
# sidebars that link to author and location archive pages.
html_sidebars = {
    "**": [
        # "about.html",
        # "navigation.html",
        "recentposts.html",
        "tagcloud.html",
        "categories.html",
        "archives.html",
        "postcard.html",  # NOTE: This should always be last in this list
    ],
}

# -- Blog Feed Options --------------------------------------------------------

# Turn feeds by setting :confval:`blog_baseurl` configuration variable.
# Choose to create feeds per author, location, tag, category, and year,
# default is ``False``.
# blog_feed_archives = False

# Choose to display full text in blog feeds, default is ``False``.
# blog_feed_fulltext = False

# Blog feed subtitle, default is ``None``.
# blog_feed_subtitle = None

# Choose to feed only post titles, default is ``False``.
# blog_feed_titles = False

# Specify custom Jinja2 templates for feed entry elements:
#     `title`, `summary`, or `content`
# For example, to add an additional feed for posting to social media:
# blog_feed_templates = {
#     # Use defaults, no templates
#     "atom": {},
#     # Create content text suitable posting to social media
#     "social": {
#         # Format tags as hashtags and append to the content
#         "content": "{ title }{% for tag in post.tags %}"
#         " #{ tag.name|trim()|replace(' ', '') }"
#         "{% endfor %}",
#     },
# }
# Default: Create one `atom.xml` feed without any templates
# blog_feed_templates = {"atom": {} }

# Specify number of recent posts to include in feeds, default is ``None``
# for all posts.
# blog_feed_length = None

# -- Font-Awesome Options -----------------------------------------------------

# ABlog templates will use of Font Awesome icons if one of the following
# is ``True``

# Link to `Font Awesome`_ at `Bootstrap CDN`_ and use icons in sidebars
# and post footers.  Default: ``None``
# fontawesome_link_cdn = None

# Sphinx_ theme already links to `Font Awesome`_.  Default: ``False``
# fontawesome_included = False

# Alternatively, you can provide the path to `Font Awesome`_ :file:`.css`
# with the configuration option: fontawesome_css_file
# Path to `Font Awesome`_ :file:`.css` (default is ``None``) that will
# be linked to in HTML output by ABlog.
# fontawesome_css_file = None

# -- Disqus Integration -------------------------------------------------------

# You can enable Disqus_ by setting ``disqus_shortname`` variable.
# Disqus_ short name for the blog.
# disqus_shortname = None

# Choose to disqus pages that are not posts, default is ``False``.
# disqus_pages = False

# Choose to disqus posts that are drafts (without a published date),
# default is ``False``.
# disqus_drafts = False

# -- Sphinx Options -----------------------------------------------------------

# If your project needs a minimal Sphinx version, state it here.
needs_sphinx = "1.2"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx_rtd_theme",
    "myst_parser",
    "ablog",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates", ablog.get_html_templates_path()]

# The suffix(es) of source filenames.
source_suffix = [".rst", ".md"]

# The encoding of source files.
source_encoding = "utf-8"

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "Mike Mabey"
copyright = f"2015-{date.today().strftime('%Y')}, Mike Mabey"
author = "Mike Mabey"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ""
# The full version, including alpha/beta/rc tags.
release = ""

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = "%b %d, %Y"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = [""]

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = "Mike Mabey"
html_favicon = "_static/favicon.ico"
html_static_path = ["_static"]
# html_extra_path = ["other/"]
html_last_updated_fmt = "%B %d, %Y"
html_copy_source = False

html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "collapse_navigation": False,
    "display_version": False,
}
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_css_files = ["custom.css"]

# Output file base name for HTML help builder.
htmlhelp_basename = "MikeMabeydoc"
