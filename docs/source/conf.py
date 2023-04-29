# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'OCTOPUS database'
copyright = '2023, OCTOPUS database (CC BY 4.0)'
author = 'Henry Munack, Emma Rehn, Wanchese M. Saktura, Alexandru T. Codilean'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = "logo.png"
html_theme_options = {
    'logo_only': False,
    'display_version': True
}

# -- Options for EPUB output
epub_show_urls = 'footnote'
