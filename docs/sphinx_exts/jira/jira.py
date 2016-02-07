# -*- coding: utf-8 -*-
'''
Sphinx/docutils extension to create links to Shape Jira.

'''

import urllib
from docutils import nodes, utils

def make_jira_link(name, rawtext, text, lineno, inliner,
                      options={}, content=[]):

    base_url = 'http://jira.shape/browse/'

    ref = base_url + text

    if "?" in text:
        title = "[Link to Jira]"
    else:
    	title = text

    node = nodes.reference(rawtext, title, refuri=ref, **options)
    return [node],[]

def setup(app):
    app.add_role('jira', make_jira_link)
