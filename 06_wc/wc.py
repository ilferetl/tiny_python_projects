#!/usr/bin/env python3
"""
Author : angelicabullard <angelicabullard@localhost>
Date   : 2020-11-22
Purpose: Emulate wc (Word Count)
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file(s)',
                        metavar='FILE',
                        type=argparse.FileType('rt'),  # argparse validates it is a readable txt file
                        nargs='*',  # zero or more
                        default=[sys.stdin])  # default is a list w/stdin, this is an open fh

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Actually do the things"""

    args = get_args()

    tot_lines = 0
    tot_words = 0
    tot_bytes = 0

    for fh in args.file:  # fh variable - reminder, this is an open file handle, can be directly read
        num_lines = 0       # inside the file loop, this will reset for each file
        num_words = 0
        num_bytes = 0
        for line in fh:  # loop over the lines, within the loop of files
            # process the line
            num_words += len(line.split())  # split the string on spaces, counting 'words'
            num_bytes += len(line)  # count of characters in the line
            num_lines += 1  # count over the lines
        tot_lines += num_lines
        tot_words += num_words
        tot_bytes += num_bytes

        print((f'{num_lines:8}{num_words:8}{num_bytes:8} {fh.name}'))

    if len(args.file)>1:
        print(f'{tot_lines:8}{tot_words:8}{tot_bytes:8} total')


# --------------------------------------------------
if __name__ == '__main__':
    main()
