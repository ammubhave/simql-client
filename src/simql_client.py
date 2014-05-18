#! /usr/bin/env python
"""SimQL Client script to process incoming SimQL query"""
import sys
import argparse


def prompter():
    from constants import GOODBYE_MESSAGE, PROMPT
    try:
        while True:
            cmd = raw_input('{0}> '.format(PROMPT)).strip()

    except ExitException:
        print GOODBYE_MESSAGE


def main():
    """ Main entry point for the script."""
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument('--token')
    parser.add_argument('--execute', '-e')

    args = parser.parse_args()
    if args.execute is None:
        prompter()
    else:
        print args.execute

if __name__ == '__main__':
    sys.exit(main())
