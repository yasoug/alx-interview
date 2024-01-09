#!/usr/bin/python3
""" Module for the canUnlockAll funct (lockboxes Task) """


def canUnlockAll(boxes):
    """
    Returns :
        True : if all boxes can be opened
        False : if not
    """
    if not boxes:
        return False
    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box not in keys and box < len(boxes):
                keys.append(box)
    if len(keys) == len(boxes):
        return True
    return False
