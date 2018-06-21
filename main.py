#!/usr/bin/env python3

import argparse


def main():
    parser = argparse.ArgumentParser(
        description='''
          Generate an RSS-feed of media files (probably audio) to be able to
          listen to audiobooks and friends in a podcast-player.
        '''
    )

    parser.add_argument('-i', '--inputs', action='store', nargs='*',
                        help='input files in the order that you want them.')

    parser.add_argument('-o', '--output', action='store',
                        help='output file, use same dir as inputs live in.')

    args = parser.parse_args()

    print(args.inputs)
    print(args.output)


if __name__ == '__main__':
    main()
