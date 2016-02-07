#!/usr/bin/env python
# -%- coding: utf-8 -%-

import os.path as osp
from sphinx.jinja2glue import BuiltinTemplateLoader


def remove_ext(path):

    return osp.splitext(path)[0]


class TemplateBridge(BuiltinTemplateLoader):

    def init(self, builder,  *args, **kwargs):

        super(TemplateBridge, self).init(builder, *args, **kwargs)
        self.environment.filters['remove_ext'] = remove_ext
        self.environment.globals['google_drive_save_url'] = builder.config['google_drive_save_url']
