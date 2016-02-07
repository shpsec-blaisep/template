#!/usr/bin/env python
# -%- coding: utf-8 -%-

from .builders.html import HTMLBuilder


def setup(app):

    app.add_config_value('google_drive_save_url', '#', True)
    app.add_javascript('save_to_drive.js')
    app.add_stylesheet('save_to_drive.css')
    app.add_builder(HTMLBuilder)
