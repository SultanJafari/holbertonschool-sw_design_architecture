#!/usr/bin/python3
"""
Module containing the canUnlockAll function to solve the lockboxes puzzle.
"""


def canUnlockAll(boxes):
    """Determines if all the locked boxes can be opened.

    Args:
        boxes (list of lists): A list containing lists of keys.

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    if not boxes:
        return True

    n = len(boxes)
    unlocked = {0}
    keys = [0]

    while keys:
        current_box = keys.pop()
        for key in boxes[current_box]:
            if key < n and key not in unlocked:
                unlocked.add(key)
                keys.append(key)

    return len(unlocked) == n
