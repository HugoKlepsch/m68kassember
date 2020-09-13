import argparse
import logging
from typing import List

from assembler.parse.parse import parse


def assemble_file(file_contents: str) -> bytes:
    """
    Assemble the given code string
    :param file_contents: Contents of the file to assemble
    :return: The assembled bytes
    """
    _tokens = parse(file_contents)
    return ''.encode('utf-8')  # TODO actually do the assembly


def assemble_files(files: List[open]) -> bytes:
    """
    Assemble given files into a series of bytes
    :param files: The files to assemble
    :return: The assembled bytes
    """
    return b''.join((assemble_file(f.read()) for f in files))


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

    for file in args.files:
        file.close()
