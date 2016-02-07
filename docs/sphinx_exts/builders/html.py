#!/usr/bin/env python
# -%- coding: utf-8 -%-


from sphinx.jinja2glue import BuiltinTemplateLoader
from sphinx.builders.html import StandaloneHTMLBuilder


class HTMLBuilder(StandaloneHTMLBuilder):
    """
    Standalone builder which does not copy source files.
    """

    name = 'html_no_copysource'
    copysource = False
