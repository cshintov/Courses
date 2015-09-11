"""
Student facing implement of solitaire version of Mancala - Tchoukaillon

Goal: Move as many seeds from given houses into the store

In GUI, you make ask computer AI to make move or click to attempt a legal move
"""


class SolitaireMancala:
    """
    Simple class that implements Solitaire Mancala
    """

    def __init__(self):
        """
        Create Mancala game with empty store and no houses
        """
        self._board = [0]

    def set__board(self, configuration):
        """
        Take the list configuration of initial number of seeds for given houses
        house zero corresponds to the store and is on right
        houses are number in ascending order from right to left
        """
        self._board = configuration[:]

    def __str__(self):
        """
        Return string representation for Mancala _board
        """
        return  str(self._board[::-1])

    def get_num_seeds(self, house_num):
        """
        Return the number of seeds in given house on _board
        """
        return self._board[house_num]

    def is_game_won(self):
        """
        Check to see if all houses but house zero are empty
        """
        if sum(self._board[1:]) > 0 :
            return False
        return True

    def is_legal_move(self, house_num):
        """
        Check whether a given move is legal
        """
        if house_num != self._board[house_num] or house_num == 0:
            return False
        return True
    
    
    def apply_move(self, house_num):
        """
        Move all of the stones from house to lower/left houses
        Last seed must be played in the store (house zero)
        """
        if house_num == 0:
            return

        self._board[house_num] = 0
        for house in range(house_num):
            self._board[house] += 1

    def choose_move(self):
        """
        Return the house for the next shortest legal move
        Shortest means legal move from house closest to store
        Note that using a longer legal move would make smaller illegal
        If no legal move, return house zero
        """
        legal_move = 0
        for house in range(1,len(self._board)):
            if self.is_legal_move(house):
                legal_move = house
                break

        return legal_move

    def plan_moves(self):
        """
        Return a sequence (list) of legal moves based on the following heuristic: 
        After each move, move the seeds in the house closest to the store 
        when given a choice of legal moves
        Not used in GUI version, only for machine testing
        """
        dup_game = SolitaireMancala()
        dup_game.set__board(self._board[:])
        winning_moves = []
        while not dup_game.is_game_won():
            prev__board = dup_game._board[:]
            house = dup_game.choose_move()
            if house != 0:
                winning_moves.append(house)
                dup_game.apply_move(house)
            if prev__board == dup_game._board:
                break
        return winning_moves
    
    
# Create tests to check the correctness of your code

def test_mancala():
    """
    Test code for Solitaire Mancala
    """

    my_game = SolitaireMancala()
    #print "Testing init - Computed:", my_game, "Expected: [0]"
        
    #print 'initial configuration',config1
    config2 = [0,1,2,3,4,5,6]
    my_game.set__board(config2)   
    
    print "Initial _board- Computed:", str(my_game), "Expected:", str([6, 5, 4, 3, 2, 1, 0])
    #print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(1), "Expected:", config1[1]
    #print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(3), "Expected:", config1[3]
    #print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(5), "Expected:", config1[5]
    #print "Testing if Won? Computed:", my_game.is_game_won(), "Expected:", False
    #print "Testing if legal move? Computed:", my_game.is_legal_move(5), "Expected:", True
    #print "Testing choose move - Computed:", my_game.choose_move(), "Expected:", 5
    #my_game.apply_move(5)
    #print "Testing apply move 5 Computed:", str(my_game), "Expected:", str([0,0,4,2,2,1,1])
    #moves = my_game.plan_moves()
    #print "Testing plan moves - Computed:",moves , "Expected:", str([3,2])
    
    # add more tests here

test_mancala()
#Import GUI code once you feel your code is correct
#import poc_mancala_gui
#poc_mancala_gui.run_gui(SolitaireMancala())

