# -*- coding: utf-8 -*-

"""A module to convert cryptographic keys to human-readable passphrases, and
back again.
"""

from __future__ import absolute_import
from __future__ import print_function

__author__ = 'Alex Willmer'
__email__ = 'alex@moreati.org.uk'
__version__ = '0.1.1'

__all__ = [
    'MAX_PASSPHRASE_SIZE',
    'WORD_LIST',
    'bytes_to_passphrase',
    'passphrase_to_bytes',
    'generate_passphrase',
]

import bisect
import os

from niceware.wordlist import WORD_LIST

MAX_PASSPHRASE_SIZE = 1024  # Max size of passphrase in bytes


def bytes_to_passphrase(bytes_):
    r"""Encode a sequence of bytes as a passphrase.

    bytes_ - a bytes-like object, or a sequence of byte values (integers 0
             to 255). The sequence must have an even length.

    Each word will encode 2 bytes from the byte seq.

    >>> bytes_to_passphrase(b'\xf2\x87\x9f\x85\x00 d\xca')
    ['upbraid', 'personalism', 'achene', 'holer']

    >>> bytes_to_passphrase([242, 135, 159, 133, 0, 32, 100, 202])
    ['upbraid', 'personalism', 'achene', 'holer']
    """
    try:
        length = len(bytes_)
    except TypeError:
        raise TypeError('Input must be a sequence of bytes')

    if length % 2 == 1:
        raise ValueError('Only even sized byte sequences are supported.')

    byteseq = bytearray(bytes_)
    words = []
    for index, byte in enumerate(byteseq[:-1:2]):
        index = index * 2
        next_byte = byteseq[index + 1]
        word_index = byte * 256 + next_byte
        word = WORD_LIST[word_index]
        words.append(word)
    return words


def passphrase_to_bytes(passphrase):
    r"""Decode a passphrase back to a bytes object.

    passphrase -- a sequence of words, each from the niceware word list.

    Each word will decode to 2 bytes of the returned byte sequence

    >>> passphrase_to_bytes(['upbraid', 'personalism', 'achene', 'holer'])
    ... #doctest: +ALLOW_BYTES
    b'\xf2\x87\x9f\x85\x00 d\xca'
    """
    byteseq = bytearray(len(passphrase) * 2)

    for index, word in enumerate(passphrase):
        word_lowercase = word.lower()
        word_index = bisect.bisect_left(WORD_LIST, word_lowercase)

        if (word_index == len(WORD_LIST)
                or WORD_LIST[word_index] != word_lowercase):
            raise ValueError('Invalid word at index {0}: {1}'
                             .format(index, word))

        byteseq[2 * index] = word_index // 256
        byteseq[2 * index + 1] = word_index % 256

    return bytes(byteseq)


def generate_passphrase(size):
    """Generate a random passphrase with the specified number of bytes.

    size -- the number of bytes to generate, must be even.

    The passphrase will contain size/2 words, and possess size*8 bits of
    entropy.

    >>> generate_passphrase(8) #doctest: +SKIP
    ['upbraid', 'personalism', 'achene', 'holer']
    """
    size = int(size)
    if size < 0 or size > MAX_PASSPHRASE_SIZE:
        raise ValueError('Size must be between 0 and {0} bytes'
                         .format(MAX_PASSPHRASE_SIZE))

    bytestring = os.urandom(size)
    return bytes_to_passphrase(bytestring)
