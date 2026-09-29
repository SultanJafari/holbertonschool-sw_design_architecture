#!/usr/bin/python3


def canUnlockAll(boxes):
    """Determines if all the locked boxes can be opened."""
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
