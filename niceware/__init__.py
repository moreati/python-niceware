# -*- coding: utf-8 -*-

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


def bytes_to_passphrase(s):
    """Convert a sequence of bytes to passphrase.
    """
    try:
        length = len(s)
    except TypeError:
        raise TypeError('Input must be a sequence of bytes')

    if length % 2 == 1:
        raise ValueError('Only even sized byte sequences are supported.')

    byteseq = bytearray(s)
    words = []
    for index, byte in enumerate(byteseq[:-1:2]):
        index = index * 2
        next_byte = byteseq[index + 1]
        word_index = byte * 256 + next_byte
        word = WORD_LIST[word_index]
        words.append(word)
    return words


def passphrase_to_bytes(words):
    """Convert a passphrase back to a bytes object.
    """
    byteseq = bytearray(len(words) * 2)

    for index, word in enumerate(words):
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
    """
    size = int(size)
    if size < 0 or size > MAX_PASSPHRASE_SIZE:
        raise ValueError('Size must be between 0 and {0} bytes'
                         .format(MAX_PASSPHRASE_SIZE))

    bytestring = os.urandom(size)
    return bytes_to_passphrase(bytestring)
