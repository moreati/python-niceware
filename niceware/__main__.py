# -*- coding: utf-8 -*-

"""Utility for generating memorable passwords"""

from __future__ import absolute_import
from __future__ import print_function


import argparse
import sys

import niceware


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--count', '-c',
                        type=int, metavar='N', default=1,
                        help="Number of passphrases to generate")
    parser.add_argument('--length', '-l',
                        type=int, metavar='N', default=16,
                        help="Number of words in each passphrase")

    args = parser.parse_args(args)
    size = 2 * args.length

    for i in range(args.count):
        passphrase = niceware.generate_passphrase(size)
        print(' '.join(passphrase))


if __name__ == '__main__':
    main()
