#!/usr/bin/env python
# -%- coding: utf-8 -%-

from sphinx_exts.builders.shape_latex import ShapeLaTeXBuilder
from sphinx_clatex.builder import setup as clatex_setup


def setup(app):
    clatex_setup(app)
    app.add_builder(ShapeLaTeXBuilder)
