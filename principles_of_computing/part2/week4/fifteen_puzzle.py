"""
Loyd's Fifteen puzzle - solver and visualizer
Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors
"""

#import poc_fifteen_gui

LEFT = 0
RIGHT = 1
R_TOP= 2

class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """

    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid != None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]

    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        ans = ""
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans

    #####################################
    # GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ########################################################
    # Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers        
        """
        solved_value = (solved_col + self._width * solved_row)
        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return (row, col)
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                assert zero_row > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction

    ##################################################################
    # Phase one methods

    def lri_helper(self, target_row, target_col):
        """ checks right tiles and rows below the target tail """
        if self.current_position(target_row, target_col) != (target_row, target_col):
            return False
        next_row, next_col = self.next_tail(target_row, target_col)
        if (next_row, next_col) == (target_row, target_col):
            return True
        else:
            return self.lri_helper(next_row, next_col)

    def next_tail(self, target_row, target_col):
        """ returns the next tail to check if it exists """
        if target_col < self.get_width() - 1:
            return target_row, target_col + 1
        elif target_row < self.get_height() - 1:
            return target_row + 1, 0
        return target_row, target_col

    def lower_row_invariant(self, target_row, target_col):
        """
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1)
        Returns a boolean
        """
        if self.get_number(target_row, target_col) is not 0:
            return False

        next_row, next_col = self.next_tail(target_row, target_col)
        if (next_row, next_col) != (target_row, target_col):
            return self.lri_helper(next_row, next_col)
        else:
            return True

    def solved(self, trow, tcol):
        """ checks whether target tile is solved """
        if (trow, tcol) == self.current_position(trow, tcol):
            return True
        else:
            return False
    
    def move_zero(self, trow, tcol):
        """ move zero to trow, tcol """
        move_string = ""
        zrow, zcol = self.current_position(0, 0)
        if trow < zrow:
            move_string += "u" * abs(trow - zrow)
        else:
            move_string += "d" * abs(trow - zrow)
        if tcol< zcol:
            move_string += "l" * abs(tcol - zcol)
        else:
            move_string += "r" * abs(tcol - zcol)
        self.update_puzzle(move_string)
        return move_string
   
    def valid_move(self, zero_row, zero_col, direction):
        """ check whether a move is valid """ 
        if direction == "l":
            if zero_col > 0:
                return True
        elif direction == "r":
            if zero_col < self._width - 1:
                return True
        elif direction == "u":
            if zero_row > 0:
                return True
        elif direction == "d":
            if zero_row < self._height - 1:
                return True
        return False
    
    def zero_position(self, c_row, c_col):
        """ returns LEFT, RIGHT , R_CORNER based on the zero tile position """
        z_row, z_col = self.current_position(0, 0)
        if z_col < c_col:
            return LEFT
        elif z_row == 0:
            return R_TOP
        else:
            return RIGHT
        
    def move_to_column(self, t_row, t_col):
        """ moves the target tile to the correct column """
        move_string = ""
        c_row, c_col = self.current_position(t_row, t_col)
        pos = self.zero_position(c_row, c_col)
        if pos == LEFT:
            while(t_col != self.current_position(t_row, t_col)[1]):
                move_string += "drrul"
                self.update_puzzle("drrul")
        elif pos == R_TOP:
            while(t_col != self.current_position(t_row, t_col)[1]):
                move_string += "dllur"
                self.update_puzzle("dllur")
        elif pos == RIGHT:
            while(t_col != self.current_position(t_row, t_col)[1]):
                move_string += "ulldr"
                self.update_puzzle("ulldr")

        return move_string

    def move_to_row(self, t_row, t_col):
        """ moves teh target tile to the correct row """
        move_string = ""
        c_row, c_col = self.current_position(t_row, t_col)
        pos = self.zero_position(c_row, c_col)
        if pos == LEFT:
            move_string += "dru"
            self.update_puzzle("dru")
            while(t_row != self.current_position(t_row, t_col)[0]):
                move_string += "lddru"
                self.update_puzzle("lddru")
        else:
            move_string += "dlu"
            self.update_puzzle("dlu")
            while(t_row != self.current_position(t_row, t_col)[0]):
                move_string += "lddru"
                self.update_puzzle("lddru")

        return move_string

    def solve_interior_tile(self, t_row, t_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        check_inv(self, t_row, t_col)
        c_row, c_col = self.current_position(t_row, t_col)
        move_string = self.move_zero(c_row, c_col)
        if(t_col != self.current_position(t_row, t_col)[1]):
            move_string += self.move_to_column(t_row, t_col)
        if(t_row != self.current_position(t_row, t_col)[0]):
            move_string += self.move_to_row(t_row, t_col)
        if t_col - 1 != self.current_position(0,0)[1]:
            move_string += "ld"
            self.update_puzzle("ld")
            print "ld"
        check_inv(self, t_row, t_col - 1)
        return move_string
    
    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        # replace with your code
        return ""

    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # replace with your code
        return False

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # replace with your code
        return False

    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        # replace with your code
        return ""

    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        # replace with your code
        return ""

    ###########################################################
    # Phase 3 methods

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        # replace with your code
        return ""

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        # replace with your code
        return ""


def check_inv(self, row, col):
    """ asserts the invariant """
    assert self.lower_row_invariant(row, col)

# Start interactive simulation
#poc_fifteen_gui.FifteenGUI(Puzzle(4, 4))


