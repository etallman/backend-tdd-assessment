#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "???"

import unittest
import sys
import argparse

def toUpper(str):
    print(str.upper)
    return str.upper()

def toLower(str):
    print(str.lower)
    return str.lower()

def toTitle(str):
    print(str.title)
    return str.title()

def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(
        description='Perform transformation on input text.')
    parser.add_argument("text", help="text to be manipulated")
    parser.add_argument("-u", "--upper",
                        help="convert text to uppercase", action="store_true")
    parser.add_argument("-l", "--lower",
                        help="convert text to lowercase", action="store_true")
    parser.add_argument("-t", "--title",
                        help="convert text to titlecase",
                        action="store_true")
    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    ns = parser.parse_args(args)
    
    text = ns.text
    if ns.lower:
        text = text.lower()
    if ns.upper:
        text = text.upper()
    if ns.title:
        text = text.title()
    return text

if __name__ == '__main__':
    print(main(sys.argv[1:]))