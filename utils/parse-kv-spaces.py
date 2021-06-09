#!/usr/bin/env python3

import sys


def parse_line(line):
    space_position = line.find(" ")

    return '"' + line[0:space_position] + '": "' + \
           line[space_position + 1:] + '"'


def parse(filename):
    print("{")

    separator = ""
    with open(filename) as fd:
        for line in fd:
            print(separator + parse_line(line.strip()))

            if separator == "":
                separator = ","

    print("}")


if __name__ == "__main__":
    try:
        file_to_parse = sys.argv[1]
    except IndexError:
        print("Usage:", sys.argv[0], "<filename>", file=sys.stderr)
        sys.exit(1)

    parse(file_to_parse)
