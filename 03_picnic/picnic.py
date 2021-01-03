#!/usr/bin/env python3
"""
Author : angelicabullard <angelicabullard@localhost>
Date   : 2020-11-18
Purpose: going on a picnic, need to know what to bring!
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',  # the positional parameter name
                        metavar='str',
                        nargs='+',  # number of arguments where + means one or more
                        help='Item(s) to bring')

    parser.add_argument('-s',  # short flag name
                        '--sorted',  # long flag name
                        action='store_true',  # if the flag is present, store a True val, default False
                        help='Sort the items'
                        )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """AB kinda funkyway of doing it, with long strings on each if/elif"""

    args = get_args()
    items = args.item
    sorted_flag = args.sorted

    if sorted_flag:  # checks if the sorted flag was used; didn't really need the var but it works
        items.sort()

    if len(items) == 1:
        print(f'You are bringing {items[0]}.')
    elif len(items) == 2:
        print(f'You are bringing {items[0]} and {items[1]}.')
    elif len(items) > 2:
        mid_items = ', '.join(items[1:-1])
        print(f'You are bringing {items[0]}, {mid_items}, and {items[-1]}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
