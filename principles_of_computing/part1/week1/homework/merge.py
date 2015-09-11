"""
Merge function for 2048 game.
codesculptor url:http://www.codeskulptor.org/#user40_RhTGnlrXV5_0.py
"""


def push_left(result):
    """
    pushes all the non-empty slides to the left
    """
    for index, slide in enumerate(result):
        if slide == 0:
            for in_index, in_slide in enumerate(result[index+1:]):
                if in_slide > 0:
                    result[index] = in_slide
                    result[in_index + index + 1] = 0
                    break


def merge(line):
    """
    Function that merges a single row or column in 2048.
    line :type list.
    """
    result = line[:]
    push_left(result)
    for index, tile in enumerate(result):
        if tile > 0:
            for inr_index, inr_tile in enumerate(result[index+1:]):
                if inr_tile == tile:
                    result[index] = tile + inr_tile
                    result[inr_index + index + 1] = 0
                    break
                else:
                    break
    push_left(result)
    return result
