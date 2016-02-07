#!/usr/bin/env python
# -%- coding: utf-8 -%-

from .builders.slatex import sLaTeXBuilder


def setup(app):

    app.add_builder(sLaTeXBuilder)
