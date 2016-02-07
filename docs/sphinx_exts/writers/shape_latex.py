#!/usr/bin/env python
# -%- coding: utf-8 -%-


from docutils import nodes
from sphinx import addnodes
from sphinx.locale import _
from sphinx.highlighting import PygmentsBridge
from sphinx.util import texescape
from sphinx.writers.latex import (
    LaTeXWriter,
    Table,
)
from sphinx_clatex.writer import (
    BEGIN_DOC,
    CustomLaTeXTranslator,
)


if not texescape.tex_escape_map:
    texescape.init()

texescape.tex_escape_map[ord(u'&')] = u'\\&{}'
texescape.tex_escape_map[ord(u'%')] = u'\\%{}'


class ShapeLaTeXTranslator(CustomLaTeXTranslator):

    def visit_document(self, node):
        """
        Comparing to the standard builder do not add `\phantomsection`.
        """
        self.footnotestack.append(self.collect_footnotes(node))
        self.curfilestack.append(node.get('docname', ''))
        if self.first_document == 1:
            # the first document is all the regular content ...
            self.body.append(BEGIN_DOC % self.elements)
            self.first_document = 0
        elif self.first_document == 0:
            # ... and all others are the appendices
            self.body.append(u'\n\\appendix\n')
            self.first_document = -1
        # "- 1" because the level is increased before the title is visited
        self.sectionlevel = self.top_sectionlevel - 1

    def visit_field_list(self, node):
        self.body.append('\n\\begin{description}\n')
        if self.table:
            self.table.has_problematic = True

    def depart_field_list(self, node):
        self.body.append('\\end{description}\n')

    def visit_block_quote(self, node):
        # If the block quote contains a single object and that object
        # is a list, then generate a list not a block quote.
        # This lets us indent lists.
        done = 0
        if len(node.children) == 1:
            child = node.children[0]
            if isinstance(child, nodes.bullet_list) or \
                    isinstance(child, nodes.enumerated_list) or \
                    isinstance(child, nodes.definition_list):
                done = 1
        if not done:
            self.body.append('\\begin{quote}\n')
            if self.table:
                self.table.has_problematic = True

    def depart_block_quote(self, node):
        done = 0
        if len(node.children) == 1:
            child = node.children[0]
            if isinstance(child, nodes.bullet_list) or \
                    isinstance(child, nodes.enumerated_list) or \
                    isinstance(child, nodes.definition_list):
                done = 1
        if not done:
            self.body.append('\\end{quote}\n')

    def visit_compound(self, node):
        pass

    def visit_sectiontoc(self, node):

        self.body.append('\n\\sectiontoc\n')

    def depart_sectiontoc(self, node):
        pass

    def depart_title(self, node):

        CustomLaTeXTranslator.depart_title(self, node)
        parent = node.parent
        if isinstance(parent, nodes.section) and self.sectionlevel == 1:
            def has_content(node):
                try:
                    secondnode = node.children[1]
                except IndexError:
                    return False
                if isinstance(secondnode, nodes.section):
                    return False
                elif isinstance(secondnode, addnodes.start_of_file):
                    return not isinstance(secondnode.children[0], nodes.section)
                else:
                    return True
            if not has_content(parent):
                self.body.append('\n\\nocontent\n')

    def visit_literal_block(self, node):
        if self.in_footnote:
            raise UnsupportedError('%s:%s: literal blocks in footnotes are '
                                   'not supported by LaTeX' %
                                   (self.curfilestack[-1], node.line))
        if node.rawsource != node.astext():
            # most probably a parsed-literal block -- don't highlight
            self.body.append('\\begin{alltt}\n')
        else:
            code = node.astext().rstrip('\n')
            code = code.replace(u"”", u"\"") \
                .replace(u"“", u"\"") \
                .replace(u"–", u"--") \
                .replace(u"’", u"'")
            self.body.append(
                u"\n\\begin{{codeblock}}{{}}\n{}\n\\end{{codeblock}}\n".format(code)
            )
            raise nodes.SkipNode

    def visit_table(self, node):
        if self.table:
            raise UnsupportedError(
                '%s:%s: nested tables are not yet implemented.' %
                (self.curfilestack[-1], node.line or ''))
        self.table = Table()
        self.table.rowcount_all = len(node.traverse(nodes.row))
        try:
            thead = node.traverse(nodes.thead)[0]
        except IndexError:
            self.table.headrowcount = None
        else:
            self.table.headrowcount = len(thead.traverse(nodes.row))
        self.table.longtable = 'longtable' in node['classes']
        self.tablebody = []
        self.tableheaders = []
        # Redirect body output until table is finished.
        self._body = self.body
        self.body = self.tablebody

    def depart_table(self, node):
        if self.table.rowcount > 30:
            self.table.longtable = True
        self.body = self._body
        if not self.table.longtable and self.table.caption is not None:
            self.body.append(u'\n\n\\begin{table}[H]\n'
                             u'\\caption{%s}\n' % self.table.caption)
            for id in self.next_table_ids:
                self.body.append(self.hypertarget(id, anchor=False))
            if node['ids']:
                self.body.append(self.hypertarget(node['ids'][0], anchor=False))
            self.next_table_ids.clear()
        if self.table.longtable:
            self.body.append('\n\\begin{longtable}')
            endmacro = '\\end{longtable}\n\n'
        elif self.table.has_verbatim:
            self.body.append('\n\\begin{tabular}')
            endmacro = '\\end{tabular}\n\n'
        elif self.table.has_problematic and not self.table.colspec:
            # if the user has given us tabularcolumns, accept them and use
            # tabulary nevertheless
            self.body.append('\n\\begin{tabular}')
            endmacro = '\\end{tabular}\n\n'
        else:
            self.body.append('\n\\begin{tabulary}{\\linewidth}')
            endmacro = '\\end{tabulary}\n\n'
        if self.table.colspec:
            self.body.append(self.table.colspec)
        else:
            if self.table.has_problematic:
                colwidth = 0.95 / self.table.colcount
                colspec = ('p{%.3f\\linewidth}' % colwidth) * \
                    self.table.colcount
                self.body.append('{{{}}}\n'.format(colspec))
            elif self.table.longtable:
                self.body.append(
                    '{{{}}}\n'.format('l' * self.table.colcount)
                )
            else:
                self.body.append(
                    '{{{}}}\n'.format('L' * self.table.colcount)
                )
        if self.table.longtable and self.table.caption is not None:
            self.body.append(u'\\caption{%s}' % self.table.caption)
            for id in self.next_table_ids:
                self.body.append(self.hypertarget(id, anchor=False))
            self.next_table_ids.clear()
            self.body.append(u'\\\\\n')
        if self.table.longtable:
            self.body.append('\\toprule\n')
            self.body.extend(self.tableheaders)
            self.body.append('\\endfirsthead\n\n')
            self.body.append('\\multicolumn{%s}{c}%%\n' % self.table.colcount)
            self.body.append(r'{{\textsf{\tablename\ \thetable{} -- %s}}} \\'
                             % _('continued from previous page'))
            self.body.extend(self.tableheaders)
            self.body.append('\\endhead\n\n')
            self.body.append(r'\multicolumn{%s}{r}{{\textsf{%s}}} \\'
                             % (self.table.colcount,
                                _('Continued on next page')))
            self.body.append('\n\\endfoot\n\n')
            self.body.append('\\endlastfoot\n\n')
        else:
            self.body.append('\\toprule\n')
            self.body.extend(self.tableheaders)
        self.body.extend(self.tablebody)
        self.body.append(endmacro)
        if not self.table.longtable and self.table.caption is not None:
            self.body.append('\\end{table}\n\n')
        self.table = None
        self.tablebody = None

    def depart_row(self, node):
        self.table.rowcount += 1
        self.body.append('\\\\\n')
        if any(self.remember_multirow.values()):
            linestart = 1
            for col in range(1, self.table.col + 1):
                if self.remember_multirow.get(col):
                    if linestart != col:
                        linerange = str(linestart) + '-' + str(col - 1)
                        self.body.append('\\cline{' + linerange + '}')
                    linestart = col + 1
                    if self.remember_multirowcol.get(col, 0):
                        linestart += self.remember_multirowcol[col]
            if linestart <= col:
                linerange = str(linestart) + '-' + str(col)
                self.body.append('\\cline{' + linerange + '}')
        else:
            if self.table.rowcount_all == self.table.rowcount:
                self.body.append('\\bottomrule\n')
            elif self.table.headrowcount == self.table.rowcount:
                self.body.append('\\midrule')

    def visit_entry(self, node):
        if self.table.col == 0:
            while self.remember_multirow.get(self.table.col + 1, 0):
                self.table.col += 1
                self.remember_multirow[self.table.col] -= 1
                if self.remember_multirowcol.get(self.table.col, 0):
                    extracols = self.remember_multirowcol[self.table.col]
                    self.body.append(' \multicolumn{')
                    self.body.append(str(extracols + 1))
                    self.body.append('}{|l|}{}')
                    self.table.col += extracols
                self.body.append(' & ')
        else:
            self.body.append(' & ')
        self.table.col += 1
        context = ''
        if 'morecols' in node:
            self.body.append(' \multicolumn{')
            self.body.append(str(node.get('morecols') + 1))
            if self.table.col == 1:
                self.body.append('}{|l|}{')
            else:
                self.body.append('}{l|}{')
            context += '}'
        if 'morerows' in node:
            self.body.append(' \multirow{')
            self.body.append(str(node.get('morerows') + 1))
            self.body.append('}{*}{')
            context += '}'
            self.remember_multirow[self.table.col] = node.get('morerows')
        if 'morecols' in node:
            if 'morerows' in node:
                self.remember_multirowcol[self.table.col] = node.get('morecols')
            self.table.col += node.get('morecols')
        if isinstance(node.parent.parent, nodes.thead):
            self.body.append('\\textsf{ ')
            context += '}'
        while self.remember_multirow.get(self.table.col + 1, 0):
            self.table.col += 1
            self.remember_multirow[self.table.col] -= 1
            context += ' & '
            if self.remember_multirowcol.get(self.table.col, 0):
                extracols = self.remember_multirowcol[self.table.col]
                context += ' \multicolumn{'
                context += str(extracols + 1)
                context += '}{l|}{}'
                self.table.col += extracols
        self.context.append(context)

    def encode(self, text):
        text = CustomLaTeXTranslator.encode(self, text)
        if not isinstance(text, unicode):
            decoded = True
            text = text.decode('utf-8')
        else:
            decoded = False
        text = text.replace(u"”", u"''") \
            .replace(u"“", u"``") \
            .replace(u"–", u"--") \
            .replace(u"’", u"'")
        if decoded:
            text = text.encode('utf-8')
        return text


class ShapeLaTeXWriter(LaTeXWriter):

    def translate(self):
        visitor = ShapeLaTeXTranslator(self.document, self.builder)
        self.document.walkabout(visitor)
        self.output = visitor.astext()
