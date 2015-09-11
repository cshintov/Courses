"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
#import poc_zombie_gui

# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)  
        else:
            self._human_list = []
        
    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        self._human_list = []
        self._zombie_list = []
        poc_grid.Grid.clear(self)
        
    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row, col))

    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)
          
    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        for zombie in self._zombie_list:
            yield zombie

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row,col))
        
    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)
    
    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        for human in self._human_list:
            yield human

    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """
        visited = poc_grid.Grid(self._grid_height, self._grid_width)
        max_distance = self._grid_height * self._grid_width
        distance_field = [[max_distance for dummyw in range(self._grid_width)] for dummyh in range(self._grid_height)]
        boundary = poc_queue.Queue()
        if entity_type == HUMAN:
            for human in self._human_list:
                boundary.enqueue(human)
                visited.set_full(human[0], human[1])
                distance_field[human[0]][human[1]] = 0
        else:
            for zombie in self._zombie_list:
                boundary.enqueue(zombie)
                visited.set_full(zombie[0], zombie[1])
                distance_field[zombie[0]][zombie[1]] = 0
        #print "boundary\n", boundary
        #print "visited\n", visited

        while len(boundary) != 0:
            cur = boundary.dequeue()

            for neighbor in visited.four_neighbors(cur[0], cur[1]):

                if (visited.is_empty(neighbor[0], neighbor[1]) and
                        self.is_empty(neighbor[0], neighbor[1])):

                    visited.set_full(neighbor[0], neighbor[1])
                    boundary.enqueue((neighbor[0], neighbor[1]))
                    distance_field[neighbor[0]][neighbor[1]] = distance_field[cur[0]][cur[1]] + 1

        return distance_field

    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        zdf = zombie_distance_field
        new = []
        for human in self._human_list:
            neighbors = self.eight_neighbors(*(human))
            distances = [zdf[neighbor[0]][neighbor[1]] for neighbor in neighbors if self.is_empty(*(neighbor))]
            if len(distances) > 0:
                dist = max(distances)
            else:
                new.append(human)
                continue
            destinations = [neighbor for neighbor in neighbors 
                                if zdf[neighbor[0]][neighbor[1]] == dist]
                                    
            destination = random.choice(destinations)
            cur_dist = zdf[human[0]][human[1]]
            if dist > cur_dist:
                new.append(destination)
            else :
                new.append(human)

        self._human_list = new[:]

    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        new = []
        hdf = human_distance_field
        for zombie in self._zombie_list:
            neighbors = self.four_neighbors(*(zombie))
            distances = [hdf[neighbor[0]][neighbor[1]] for neighbor in neighbors if self.is_empty(*(neighbor))]
            if len(distances) > 0:
                dist = min(distances)
            else:
                new.append(zombie)
                continue
            destinations = [neighbor for neighbor in neighbors 
                                if hdf[neighbor[0]][neighbor[1]] == dist] 
            destination = random.choice(destinations)
            cur_dist = hdf[zombie[0]][zombie[1]]
            if dist < cur_dist:
                new.append(destination)
            else:
                new.append(zombie)

        self._zombie_list = new[:]

# Start up gui for simulation - You will need to write some code above
# before this will work without errors

#poc_zombie_gui.run_gui(Apocalypse(30, 40))
#import test_suite as test
#test.run_suite(Apocalypse)
