.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
collective.faq
==============================================================================

.. image:: https://secure.travis-ci.org/collective/collective.faq.png
    :target: http://travis-ci.org/collective/collective.faq

.. image:: https://travis-ci.org/collective/collective.faq.svg?branch=master
    :target: https://travis-ci.org/collective/collective.faq

.. image:: https://coveralls.io/repos/collective/collective.faq/badge.svg
  :target: https://coveralls.io/r/collective/collective.faq

.. image:: https://landscape.io/github/collective/collective.faq/master/landscape.svg?style=flat
  :target: https://landscape.io/github/collective/collective.faq/master
  :alt: Code Health

.. image:: https://img.shields.io/pypi/v/collective.faq.svg
    :target: https://pypi.python.org/pypi/collective.faq/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/l/collective.faq.svg
    :target: https://pypi.python.org/pypi/collective.faq/
    :alt: License

|

.. image:: https://raw.githubusercontent.com/collective/collective.faq/master/kitconcept.png
   :alt: kitconcept
   :target: https://kitconcept.com/


Features
--------

- As reviewer, I can add an FAQ.
- As reviewer, I can add an FAQ item to an FAQ.
- As reviewer, I can add an FAQ item to an FAQ item.
- As reviewer, I can use rich text to create an FAQ item.
- As reviewer, I can link to an existing FAQ item.
- As anonymous user, I can see an FAQ list.
- As anonymous user, I can search the FAQ and FAQ Entry.


Installation
------------

Install collective.faq by adding it to your buildout::

   [buildout]

    ...

    eggs =
        collective.faq


and then run "bin/buildout".


Contribute
----------

- `Source code at Github <https://github.com/collective/collective.faq>`_
- `Issue tracker at Github <https://github.com/collective/collective.faq/issues>`_ or same


Support
-------

If you are having issues, `please let us know <https://github.com/collective/collective.faq/issues>`_.


Development
-----------

Requirements:

- Python 2.7
- Virtualenv

Setup::

  make

Run Static Code Analysis::

  make code-Analysis

Run Unit / Integration Tests::

  make test

Run Robot Framework based acceptance tests::

  make test-acceptance


Credits
-------

.. image:: https://www.hu-berlin.de/++resource++humboldt.logo.Logo.png
   :height: 97px
   :width: 434px
   :scale: 100 %
   :alt: HU Berlin
   :align: center
   :target: https://www.hu-berlin.de

The development of this plugin has been kindly sponsored by `Humboldt-Universität zu Berlin`_.

.. image:: https://raw.githubusercontent.com/kitconcept/pas.plugins.memberpropertytogroup/master/kitconcept.png
   :alt: kitconcept
   :target: https://kitconcept.com/

Developed by `kitconcept`_.


License
-------

The project is licensed under the GPLv2.


.. _Humboldt-Universität zu Berlin: https://www.hu-berlin.de
.. _kitconcept: http://www.kitconcept.com/
