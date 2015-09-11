"""
2048 game
"""

#import poc_2048_gui
from random import choice

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def initial(height, width):
    """
    Finds the inital tiles for each direction
    """
    initial_dir = {}
    initial_dir[UP] = traverse_grid((0, 0), (0, 1), width)
    initial_dir[DOWN] = traverse_grid((height-1, width-1), (0, -1), width)
    initial_dir[RIGHT] = traverse_grid((height-1, width-1), (-1, 0), height)
    initial_dir[LEFT] = traverse_grid((0, 0), (1, 0), height)
    return initial_dir

def traverse_grid(start_cell, direction, num_steps):
    """
    Traverses the grid from starting cell in the specified direction
    for num_steps squares
    """
    start_row, start_col = start_cell
    result = []
    for step in range(num_steps):
        row = start_row + step * direction[0]
        col = start_col + step * direction[1]
        result.append((row, col))
    return result


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

def empty_sq(grid, grid_height, grid_width):
    """
    Computes all the empty-tile-indices
    """
    rows = range(grid_height)
    cols = range(grid_width)
    empty = [(row, col) for row in rows for col in cols if grid[row][col] == 0]
    return choice(empty)

class TwentyFortyEight(object):
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._grid = []
        self._initial_tiles = initial(grid_height, grid_width)
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        row = self.get_grid_width()
        col = self.get_grid_height()
        self._grid = [[0 for dummy_cl in range(row)] for dummy_rw in range(col)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        string = "\n"
        for row in range(self.get_grid_height()):
            string += str(self._grid[row]) + '\n'
        return string

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        if direction in (UP, DOWN):
            num_steps = self.get_grid_height()
        else:
            num_steps = self.get_grid_width()

        changed = False
        for tile in self._initial_tiles[direction]:
            indices = traverse_grid(tile, OFFSETS[direction], num_steps)
            line = []
            for row, col in indices:
                line.append(self.get_tile(row, col))
            merged_line = merge(line)
            for (row, col), value in zip(indices, merged_line):
                if value != self.get_tile(row, col):
                    changed = True
                self.set_tile(row, col, value=value)
        if changed:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        height = self.get_grid_height()
        width = self.get_grid_width()
        row, col = empty_sq(self._grid, height, width)
        value = choice([2]*9+[4])
        self.set_tile(row, col, value)

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        value = self._grid[row][col]
        return value

#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
