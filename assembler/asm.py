import argparse
import logging
from typing import List


def assemble_files(files: List[open]) -> str:
    return ''


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument('files',
                            nargs='*',
                            type=open)
    arg_parser.add_argument('--verbose', '-v',
                            action='count',
                            default=0)

    args = arg_parser.parse_args()

    level = logging.WARNING
    if 0 < args.verbose <= 1:
        level = logging.INFO
    if 1 < args.verbose <= 2:
        level = logging.DEBUG
    logging.basicConfig(level=level)

    print(assemble_files(args.files))
