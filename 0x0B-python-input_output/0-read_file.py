#!/usr/bin/python3
"""Module 0-read_file.
Reads from a file and print"""


def read_file(filename=""):
    """Reads from filename and prints
    its contents to stdout.
    Args:
        - filename: name of the file
    """

    with open(filename) as f:
        read_data = f.read()
        print(read_data, end="")
