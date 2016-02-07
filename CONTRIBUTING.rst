:pdf: doctutorial

Add to the Internal Docs
========================

This tutorial will show you how to add to the Internal Doc Portal and and also create a PDF of your document.

**Bottom line:**
*The build scripts require a collection of settings which we associate with a ``doc_code`` defined in ``techdocs/source/internal_library.json``. This doc code is the argument for pdf builds.*

Add to the HTML Doc Portal
--------------------------

	1.	Clone the Stash Repo (Click **View Source in Stash** on the left-hand sidebar, to find the Stash Repo)

	2.	Create and checkout a new branch named after the associated Jira ticket (if you don't have one, make one in the DOCS project)

	3.	Add a new ReStructuredText (.rst) file in ``techdocs/source/``.

		Example::

			techdocs/source/my_supercool_doc.rst

	4.	Add the content into your file using ReStructuredText markup. You can use  our example doc as a template to start from: :download:`/common/text/my_supercool_doc.rst`. (copy and paste the contents into your RST file and use them as a starting point.)

		For a quick intro to writing ReStructuredText, check out the Sphinx documentation's `reStructured Text Primer <http://sphinx-doc.org/rest.html>`__, or the official rST documentation's `A ReStructuredText Primer <http://docutils.sourceforge.net/docs/user/rst/quickstart.html>`__.

	5.	Add your file to the Internal docs toctree. To do so, open ``source/internal/internal.rst`` in a text editor, and add the filename (without the extension) of your RST file to the ``.. toctree::`` directive.

		Example::

			.. toctree::

				my_supercool_doc
				Encyclopædia Shapetanica (High-Side) <https://docs.google.com/a/intrafile.com/document/d/1-HGvj8OzYVSaOx7aWhOVHQ4JhGhwS3tiCtpGKT-C2cw/edit?usp=sharing>
				Internal Python Modules <http://docs.shape/python>
				performance
				+ Add a New Internal Doc <internal_add>

That is all you need to do in order to get your document included in the HTML build. However, if you would like to have a PDF, you will need to complete the next set of instructions.

.. note:: For more detailed reference documents about reStructuredText, see:

		*	`ReStructuredText Markup Specification <http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html>`__
		*	`ReStructuredText Directive Reference <http://docutils.sourceforge.net/docs/ref/rst/directives.html>`__.

PDFs
----

This section tells you how to add your document to the list of docs that have PDFs, so you can easily build a PDF with our styles.

	1. Open ``techdocs/source/internal_library.json`` in your text editor.

	2. This file is a list of JSON objects. The name of the object is the ``doc_code`` for your document. Add a JSON object for your document that includes the following info:

		*	``doc_code``
		*	``master_doc``
		*	``title``
		*	``layout``
		*	``publish``
		*	``external``
		*	``doc_type`` (optional)

	For details about these values, see :ref:`portal-doc-properties``.

	**EXAMPLE 1**

	The below JSON object would generate a PDF using ``source/my_supercool_doc.rst``, using the doc_code ``cool``. It would be a "short-form" document, which is to say it will not have chapter breaks, and is likely 1-5 pages. It will have an INTERNAL watermark.

	.. code-block:: json

		"cool" : {
			"master_doc" : "internal/my_supercool_doc",
			"title" : "My New Document",
			"layout": "short-form",
			"publish": true,
			"external": false
		}

	**EXAMPLE 2**

	The JSON object below would generate a PDF using ``source/my_supercool_doc.rst``, using the doc_code ``cool``. This document would have chapter breaks, so it's probably a longer document, maybe 20-30 pages. It will have a DRAFT watermark.

	.. code-block:: json

			"cool" : {
				"master_doc" : "internal/my_supercool_doc",
				"title" : "My New Document",
				"layout": "long-form",
				"publish": false,
				"external": true
			}

Build Your PDF
``````````````

Once you’ve completed all of the above steps, all you have to do to build your doc is run the ``build_pdf.py`` script in your command line with your book's ``doc_code`` as an argument.

The build script is located at the top-level of the techdocs directory, and is called like this: ``python build_pdf.py <doc_code>``.

The current **Build Location** is: ``builds/pdf/<doc_code>/``

**Example**

Here is an example build command::

	python build_pdf.py cool

The above command would generate a PDF using ``source/my_supercool_doc.rst``, as defined in the example used throughout this document. The title will be “My New Document” and the PDF Filename will be ``My_New_Document_v160.pdf``. The build location would be ``builds/pdf/cool/``

.. _add-pdf-link:

Add a Link to the PDF to the HTML
`````````````````````````````````

To add a link to your document anywhere in the source RST, use the following markdown: ``|<doc_code>|``. So, for example, if I wanted to add the ``cool`` doc, I would type::

	Here is the PDF: |cool|.

The download link will be inserted. It will automatically have the title of your document, and include your PDF in the HTML output.

Add a PDF Button to the HTML
````````````````````````````

If you want people to be able to download your PDF directly from the HTML page, you MUST first add a link to the PDF somewhere in the HTML using the method described above (in the :ref:`add-pdf-link` section). It's preferred that you add it to the bottom of ``techdocs/source/index_internal.rst``, where there is already a list of available PDFs.

Once you've done that, you can add a PDF download button to the top of any of your HTML pages. To do so, just add a PDF meta tag (``:pdf:<doc_code>``) at the top of any source files on which you want the button to appear.

For example, the following code would add a PDF download button to the My Cool Document PDF at the top of this page::

	:pdf: cool

	My Cool Document
	================

	<text begins here>

So to be clear, you MUST add this PDF meta tag *before any other content in your source file.* Otherwise, it will 1) not work, and 2) be visible in plain-text on your HTML page and in your PDF.

Submit Your Doc
---------------

When you are done with your edits and would like me to add your docs to the portal:

	1. Submit a pull request to the ``Master`` branch.
	2. Add AlexP and Blaise as reviewers

Once your request is approved, it will show up in the next internal build at:
http://docs.shape/internal/internal_index.html

