#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_niceware
----------------------------------

Tests for `niceware` module.
"""

import pytest

import niceware


def test_generate_passphrase_returns_correct_length():
    assert len(niceware.generate_passphrase(2)) == 1
    assert len(niceware.generate_passphrase(0)) == 0
    assert len(niceware.generate_passphrase(20)) == 10
    assert len(niceware.generate_passphrase(512)) == 256

def test_generate_passphrase_raises_on_odd_number_of_bytes():
    with pytest.raises(ValueError):
        niceware.generate_passphrase(1)
    with pytest.raises(ValueError):
        niceware.generate_passphrase(23)

def test_generate_passphrase_raises_on_out_of_range():
    with pytest.raises(ValueError):
        niceware.generate_passphrase(1026)
    with pytest.raises(ValueError):
        niceware.generate_passphrase(-4)


def test_bytes_to_passphrase_raises_when_odd_length():
    with pytest.raises(ValueError):
        niceware.bytes_to_passphrase(bytearray(1))

def test_bytes_to_passphrase_raises_when_not_a_byte_sequence():
    with pytest.raises(TypeError):
        niceware.bytes_to_passphrase(1)
    with pytest.raises(ValueError):
        niceware.bytes_to_passphrase([255, 999])
    with pytest.raises(TypeError):
        niceware.bytes_to_passphrase(iter(b'ab'))

def test_bytes_to_passphrase_returns_expected_passphrases():
    assert niceware.bytes_to_passphrase(b'') == []
    assert niceware.bytes_to_passphrase([0, 0]) == ['a']
    assert niceware.bytes_to_passphrase([0xff, 0xff]) == ['zyzzyva']
    assert niceware.bytes_to_passphrase(
            [0, 0, 17, 212, 12, 140, 90, 247,
             46, 83, 254, 60, 54, 169, 255, 255]) \
            == \
            ['a', 'bioengineering', 'balloted', 'gobbledegook',
             'creneled', 'written', 'depriving', 'zyzzyva']


def test_passphrase_to_bytes_raises_when_input_is_not_in_the_wordlist():
    with pytest.raises(ValueError):
        niceware.passphrase_to_bytes(['You', 'love', 'ninetales'])

def test_passphrase_to_bytes_returns_expected_bytes():
    assert niceware.passphrase_to_bytes(['A']) == b'\x00\x00'
    assert niceware.passphrase_to_bytes(['zyzzyva']) == b'\xff\xff'
    assert niceware.passphrase_to_bytes(
            ['A', 'bioengineering', 'Balloted', 'gobbledegooK',
             'cReneled', 'Written', 'depriving', 'zyzzyva']) \
            == b'\x00\x00' b'\x11\xd4' b'\x0c\x8c' b'\x5a\xf7' \
               b'\x2e\x53' b'\xfe\x3c' b'\x36\xa9' b'\xff\xff'
