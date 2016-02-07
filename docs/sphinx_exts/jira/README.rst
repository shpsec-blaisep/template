==================================
Sphinx extention : wikipedia
==================================

This Sphinx_ extension adds a docutils role to create links to any page in Jira.

.. _Sphinx: http://sphinx-doc.org/

Enabling the extension in Sphinx
--------------------------------

To enable the use of this extension in your Sphinx project, you will need to edit ``conf.py`` file in your Sphinx project.

First, add the extension module path to ``sys.path``. ::

    sys.path.append(os.path.abspath('../../sphinx_exts/jira'))

Then, enable this extention by adding ``jira`` to the list of
``extensions``. ::

    extensions += ['jira']

Usage
-----

In your restructuredText markup, you can create links to various Jira tickets  using markup of the following format::

To link to a *RLI* article ::

    :jira:`RLI-123`

To link to a filter ::

    :jira:`filter=12345`

To link to any other Jira links, just include everything after `http://jira/browse/` in the URL ::

    :jira:`?filter=12345`

Instead of using the default text for the hyperlink, you can also specify some content to display instead ::

    :jira:`This is the best Jira Ticket Ever <RLI-123>`

