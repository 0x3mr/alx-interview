#!/usr/bin/python3
"""
Defines a UTF-8 Validation function
"""


def validUTF8(data):
    """
    UTF-8 Validation
    Args:
        data (list[int]): an array of characters represented as 1byte int
    Returns:
        (True): if all characters in data are valid UTF-8 code point
        (False): if one or more characters in data are invalid code point
    """
    i = 0
    while i < len(data):
        byte = data[i]
        if byte >> 7 == 0:
            length = 0
        elif byte >> 5 == 0b110:
            length = 1
        elif byte >> 4 == 0b1110:
            length = 2
        elif byte >> 3 == 0b11110:
            length = 3
        else:
            return False

        if i + length >= len(data):
            return False

        for j in range(i + 1, i + length + 1):
            if not (data[j] >> 6 == 0b10):
                return False

        i += length + 1

    return True
