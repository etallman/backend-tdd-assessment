#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "???"

import unittest
import sys
import argparse


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser()
#     parser.parse_args()
#     #args = parser.parse_args()

#     parser = argparse.ArgumentParser(
#         description='Perform transformation on input text.')
#     parser.add_argument("text", help="text to be manipulated")
#     parser.add_argument("-h", "--help", 
#                         help="show this help message and exit",)
#     parser.add_argument( "-u", "--upper", 
#                         help="convert text to uppercase",)
#     parser.add_argument("-l", "--lower", 
#                         help="convert text to lowercase",)
#     parser.add_argument("-t", "--title", 
#                         help="convert text to titlecase",
#                         action="store_true")
    
#     my_namespace = parser.parse_args()
#     print(my_namespace.my_optional)
    
# print(create_parser())


def main(args):
    """Implementation of echo"""
    pass

#if __name__ == '__main__':
    
#     # unittest.main()