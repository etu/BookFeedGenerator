#!/usr/bin/env python3

from feedgen.feed import FeedGenerator
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

    parser.add_argument('-b', '--base_url', action='store',
                        help='Base URL for files to build complete links.')

    args = parser.parse_args()

    generateFeed(args.inputs, args.output, args.base_url)


def generateFeed(inputFiles, outputFile, baseUrl):
    fg = FeedGenerator()
    fg.load_extension('podcast')
    fg.title(inputFiles[0])
    fg.link(href=baseUrl, rel='alternate')
    fg.description(inputFiles[0])

    for inputFile in inputFiles:
        fe = fg.add_entry()
        fe.id(inputFile)
        fe.title(inputFile)
        fe.description(inputFile)
        fe.enclosure(baseUrl + inputFile, 0, 'audio/mpeg')

    fg.rss_str(pretty=True)
    fg.rss_file(outputFile)


if __name__ == '__main__':
    main()
