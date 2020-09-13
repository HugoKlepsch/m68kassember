import argparse
import logging
from typing import List


def assemble_files(_files: List[open]) -> bytes:
    """
    Assemble given files into a series of bytes
    :param _files: The files to assemble
    :return: The assembled bytes
    """
    return ''.encode('utf-8')


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument('files',
                            nargs='*',
                            type=open)
    arg_parser.add_argument('--verbose', '-v',
                            action='count',
                            default=0)

    args = arg_parser.parse_args()

    LOG_LEVEL = logging.WARNING
    if 0 < args.verbose <= 1:
        LOG_LEVEL = logging.INFO
    if 1 < args.verbose <= 2:
        LOG_LEVEL = logging.DEBUG
    logging.basicConfig(level=LOG_LEVEL)

    print(assemble_files(args.files))
