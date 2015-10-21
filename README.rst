pyramid_ipython
===============

`IPython <http://ipython.org/>`_ bindings for
`Pyramid <http://docs.pylonsproject.org/en/latest/docs/pyramid.html>`_.

Installation
------------

::

  $ $VENV/bin/pip install pyramid_ipython

Usage
-----

Ensure the shell is available::

  $ $VENV/bin/pshell --list-shells
  Available shells:
    ipython
    python

The shell should be auto-selected when running ``pshell``::

  $ $VENV/bin/pshell development.ini

However, if there are multiple shells you can also be explicit::

  $ $VENV/bin/pshell -p ipython development.ini
