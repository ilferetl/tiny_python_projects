#!/usr/bin/env python3
"""
Author : angelicabullard <angelicabullard@localhost>
Date   : 2020-11-21
Purpose: Phone number encryption by jumping the five on a telephone keypad.
Accepts text input, changing only integers to encrypted
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='str', help='Input text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """The actual function things"""

    args = get_args()
    text = args.text
    jumper = {'1': '9', '2': '8', '3': '7', '4': '6', '5': '0',
              '6': '4', '7': '3', '8': '2', '9': '1', '0': '5'}
    output_txt = ''

    for char in text:  # loop through the text string
        if char in jumper.keys():  # if the char is found in the dictionary, replace txt
            char = jumper.get(char)
            # don't need the else statement since it will just not do anything to char
        output_txt += char

    print(f'{output_txt}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
