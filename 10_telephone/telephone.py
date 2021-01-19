#!/usr/bin/env python3
"""
Author : angelicabullard <angelicabullard@localhost>
Date   : 2021-01-09
Purpose: Do all the things
"""

import argparse
import os
import random
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Telephone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-m',
                        '--mutations',
                        help='Percent mutations',
                        metavar='mutations',
                        type=float,
                        default=0.1)

    args = parser.parse_args()

    if not 0 <= args.mutations <= 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    if os.path.isfile(args.text):  # check if the text is a file
        args.text = open(args.text).read().rstrip()  # if true, open text, read as a string and strip whitespace

    return args


# --------------------------------------------------
def main():
    """Actually do the things"""

    args = get_args()

    text = args.text
    random.seed(args.seed)
    alpha = ''.join(sorted(string.ascii_letters + string.punctuation))
    len_text = len(text)
    num_mutations = round(args.mutations * len_text)
    new_text = list(text)
    indexes = random.sample(range(len_text), num_mutations)

    for i in indexes:
        new_text[i] = random.choice(alpha.replace(new_text[i], ''))
    print('You said: "{}"\nI heard : "{}"'.format(text, ''.join(new_text)))


# --------------------------------------------------
if __name__ == '__main__':
    main()
