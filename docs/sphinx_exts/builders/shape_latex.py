#!/usr/bin/env python
# -%- coding: utf-8 -%-

from six import text_type

from docutils import nodes
from docutils.utils import new_document
from sphinx import addnodes
from sphinx.util.console import darkgreen
from sphinx_clatex.builder import LaTeXBuilder
from sphinx_exts.writers.shape_latex import ShapeLaTeXWriter
from sphinx_exts.writers import shape_latex_nodes


def inline_all_toctrees(builder, docnameset, docname, tree, colorfunc, include_maintoc=False):
    """Inline all toctrees in the *tree*.

    Record all docnames in *docnameset*, and output docnames with *colorfunc*.
    """
    tree = tree.deepcopy()
    for toctreenode in tree.traverse(addnodes.toctree):
        newnodes = []
        #if include_maintoc:
        #    newnodes.append(shape_latex_nodes.sectiontoc())
        #else:
        include_maintoc = True
        includefiles = map(text_type, toctreenode['includefiles'])
        for includefile in includefiles:
            try:
                builder.info(colorfunc(includefile) + " ", nonl=1)
                subtree = inline_all_toctrees(builder, docnameset, includefile,
                                              builder.env.get_doctree(includefile),
                                              colorfunc, include_maintoc=True)
                docnameset.add(includefile)
            except Exception:
                builder.warn('toctree contains ref to nonexisting '
                             'file %r' % includefile,
                             builder.env.doc2path(docname))
            else:
                sof = addnodes.start_of_file(docname=includefile)
                sof.children = subtree.children
                for sectionnode in sof.traverse(nodes.section):
                    if 'docname' not in sectionnode:
                        sectionnode['docname'] = includefile
                newnodes.append(sof)
        toctreenode.parent.replace(toctreenode, newnodes)
    return tree


class ShapeLaTeXBuilder(LaTeXBuilder):

    name = "shape_latex"

    WriterClass = ShapeLaTeXWriter

    def assemble_doctree(self, indexfile, toctree_only, appendices):
        self.docnames = set([indexfile] + appendices)
        self.info(darkgreen(indexfile) + " ", nonl=1)
        tree = self.env.get_doctree(indexfile)
        tree['docname'] = indexfile
        if toctree_only:
            # extract toctree nodes from the tree and put them in a
            # fresh document
            new_tree = new_document('<latex output>')
            new_sect = nodes.section()
            new_sect += nodes.title(u'<Set title in conf.py>',
                                    u'<Set title in conf.py>')
            new_tree += new_sect
            for node in tree.traverse(addnodes.toctree):
                new_sect += node
            tree = new_tree
        #  import pdbc; pdbc.set_trace()
        largetree = inline_all_toctrees(self, self.docnames, indexfile, tree,
                                        darkgreen)
        largetree['docname'] = indexfile
        for docname in appendices:
            appendix = self.env.get_doctree(docname)
            appendix['docname'] = docname
            largetree.append(appendix)
        self.info()
        self.info("resolving references...")
        self.env.resolve_references(largetree, indexfile, self)
        # resolve :ref:s to distant tex files -- we can't add a cross-reference,
        # but append the document name
        for pendingnode in largetree.traverse(addnodes.pending_xref):
            docname = pendingnode['refdocname']
            sectname = pendingnode['refsectname']
            newnodes = [nodes.emphasis(sectname, sectname)]
            for subdir, title in self.titles:
                if docname.startswith(subdir):
                    newnodes.append(nodes.Text(_(' (in '), _(' (in ')))
                    newnodes.append(nodes.emphasis(title, title))
                    newnodes.append(nodes.Text(')', ')'))
                    break
            else:
                pass
            pendingnode.replace_self(newnodes)
        return largetree
