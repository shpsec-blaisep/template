Documentation Portal Change Log
===============================

.. versionadded:: 1.7
	The following new features introduced:

		*	new architecture for internal documentation:
				-	:doc:`/internal_guides/internal_guides`
				-	:doc:`internal_ref/internal_ref`
				-	:doc:`eng_ref/eng_ref`
		*	added :doc:`Document Request </portal/request>` page
		*	documented ShapeShifter document :doc:`Types & Templates </portal/ssdocs_tutorial>`
		*	added ``adhoc`` folder for internal docs that require PDFs but should not be included in HTML Doc Portal


.. versionadded:: 1.6
	Deployed the new Internal Documentation Portal, which includes:

		*	internal release notes for all ShapeShifter releases;
		*	links to documentation for each release;
		*	internal reference documentation;
		*	in-progress documentation for unreleased products

.. versionadded:: 1.5
	Major release, which introduced:

		*	Shape_latex: custom LaTeX classes to build PDFs.
		*	View in Stash button displays the source file in Stash so that contributors can checkout, update and submit pull requests.
		*	Download as PDF button opens the PDF version of the current *book* (not the current page).


.. versionadded:: 1.4
	Added Continuous Integration with the SC2 UI project. End user docs are automatically pulled when the product is built and incorporated in the RPM hosted on Artifactory.

.. versionadded:: Shape_latex version history
	15/08/06	delete the lastpage package
	15/08/07	fix a problem with monospace font and set better proportion with sans serif (0.89)
	15/08/07	add penalty for window and orphans
	15/08/10	add a command for circ number
	15/08/10	add char for codeblock
	15/08/11	add `\SET/\db` for release and author
	15/08/24	add center foot and head
	15/08/27    add new encoding and part of the sphinx.sty code (Verbatim)
	15/09/04    add char encoding
	15/09/10    change the font
	15/09/11    fix a bug in toc for lines too long, add gray background color and fix issue to Verbatim
	15/09/18    change Verbatim background
	15/09/30    beta version to test: the manual is shapemanual.pdf

.. versionadded:: Shape LaTeX general class
	shapeform.cls	15/09/30 v1.0
	15/08/06	create a `\label{LastPage}` on atenddocument
	15/08/06	create a noCA option for short form
	15/08/06	create a new atenddocument to print the ConfAg in last page in short
	15/08/10	create the command `\nocontent` if there are no content after a section
	15/08/10	create the codeblock environment
	15/08/17	change sectioning color
	15/08/24	check watermak changes and add center foot and head
	15/09/04    add twoside/oneside option
	15/09/10    change the font and test
	15/09/11    fix a bug in toc for lines too long and set oneside as default
	15/09/30    beta version to test: the manual is shapeformmanual.pdf, longform.pdf and shortform.pdf show the layout


.. versionadded:: Shape Marketing class
	whitepaper.cls	15/09/30 v1.0
	15/08/24	correct a bug in a `\SET/\db` command
	15/09/04	fix a typo
	15/09/10    change the font and test
	15/09/30    beta version to test: the manual is whitepapermanual.pdf, whitepaper.pdf shows the layout
