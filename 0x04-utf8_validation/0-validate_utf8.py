#!/usr/bin/python3
"""validUTF8 Module"""


def validUTF8(data):
    """
    Determines if given data set represents valid UTF-8 encoding
    Returns:
        True if data is a valid UTF-8 encoding, False otherwise
    """
    bytes = 0
    for i in data:
        mask = 1 << 7
        if not bytes:
            while i & mask:
                bytes += 1
                mask >>= 1
            if bytes > 4:
                return False
        elif i >> 6 != 2:
            return False
        if bytes:
            bytes -= 1
    return bytes == 0
