#!/usr/bin/env python
# -%- coding: utf-8 -%-

import os
from os import path

from sphinx import addnodes
from sphinx.builders.latex import LaTeXBuilder
from sphinx.util.osutil import SEP

from sphinx_exts.builders.shape_latex import ShapeLaTeXBuilder


class sLaTeXBuilder(ShapeLaTeXBuilder):
    """
    LaTeX builder which builds every source file seperately.  Note that if
    a file contains a `:toctree:` directive all the documents listed in
    the toctree will be included.
    """

    name = "slatex"

    def init_document_data(self):

        self.confdir
        preliminary_document_data = []
        assert len(self.config.latex_documents) == 1
        latex_document = self.config.latex_documents[0]
        _, _, title, author, docclass = latex_document[:5]
        for docname in self.env.all_docs:
            targetname = "{}.tex".format(docname)
            dirname = path.join(self.outdir, path.dirname(targetname))
            if not path.exists(dirname):
                os.makedirs(dirname)
            preliminary_document_data.append(
                (docname, targetname, title, author, docclass, False)
            )

        if not preliminary_document_data:
            self.warn('no "latex_documents" config value found; no documents '
                      'will be written')
            return

        # assign subdirs to titles
        self.titles = []
        for entry in preliminary_document_data:
            docname = entry[0]
            if docname not in self.env.all_docs:
                self.warn('"latex_documents" config value references unknown '
                          'document %s' % docname)
                continue
            self.document_data.append(entry)
            if docname.endswith(SEP+'index'):
                docname = docname[:-5]
            self.titles.append((docname, entry[2]))

    def assemble_doctree(self, indexfile, toctree_only, appendices):
        tree = self.env.get_doctree(indexfile)
        largetree = super(sLaTeXBuilder, self).assemble_doctree(indexfile, toctree_only, appendices)
        if not tree.traverse(addnodes.toctree):
            # we need to wrap the doctree inside a `start_of_file` node which
            # needs to be visited before `document` to set `curfilestack` on
            # the `LaTeXTranslator` class.
            docname = largetree['docname']
            sof = addnodes.start_of_file(docname=docname)
            sof.reporter = largetree.reporter
            del largetree.reporter
            sof.children = [largetree]
            largetree = sof
        return largetree
