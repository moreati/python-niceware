Niceware for Python
===================

.. image:: https://img.shields.io/pypi/v/niceware.svg
        :target: https://pypi.python.org/pypi/niceware
        :alt: PyPI status

.. image:: https://img.shields.io/travis/moreati/python-niceware.svg
        :target: https://travis-ci.org/moreati/python-niceware
        :alt: Build status

.. image:: https://readthedocs.org/projects/niceware/badge/?version=latest
        :target: https://niceware.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/moreati/niceware/shield.svg
     :target: https://pyup.io/repos/github/moreati/niceware/
     :alt: Updates


A Python port of Niceware_, for generating random-yet-memorable passwords.
Each word provides 16 bits of entropy, so a useful password requires at least
3 words.

Because the wordlist is of exactly size 2^16, Niceware is also useful for converting cryptographic keys and other sequences of random bytes into human-readable phrases. With Niceware, a 128-bit key is equivalent to an 8-word phrase.

* Free software: MIT license
* Documentation: https://niceware.readthedocs.io.

Usage
-----

To insall

.. code:: console

    $ pip install niceware

To generate an 8-byte passphrase

.. code:: python

    >>> import niceware
    >>> niceware.generate_passphrase(8)
    ['deathtrap', 'stegosaur', 'nilled', 'nonscheduled']

Niceware for Python uses ``os.urandom`` for entropy.

Credits
-------

Niceware for Python is a port of Niceware_, by yan_.

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Niceware: https://github.com/diracdeltas/niceware
.. _yan: https://diracdeltas.github.io/blog/about/
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
