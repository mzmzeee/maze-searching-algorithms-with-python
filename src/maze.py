# This file contains the Maze class, which is responsible for generating the maze

# The maze is represented as a grid of cells:
# - ' ' represents an open cell
# - '#' represents a blocked cell (wall)
# - 'S' represents the start point
# - 'E' represents the exit point

# The generate_maze method creates a maze with the following steps:
# 1. Initializes all cells as open (' ')
# 2. Randomly blocks some cells based on the block probability
# 3. Sets the start and exit points, either randomly or at fixed positions
import random

class Maze:
    def __init__(self, size=25, block_prob=0.25):
        self.size = size
        self.block_prob = block_prob
        self.maze = None
        self.start = None
        self.exit = None

    def generate_maze(self, random_start_end=True):
        # Initialize the maze grid with open cells
        self.maze = [[' ' for _ in range(self.size)] for _ in range(self.size)]
        # Randomly block cells based on the block probability
        for i in range(self.size):
            for j in range(self.size):
                if random.random() < self.block_prob:
                    self.maze[i][j] = '#'
        # Set the start and exit points
        if random_start_end:
            while True:
                # Randomly select start and exit points
                sx, sy = random.randint(0, self.size-1), random.randint(0, self.size-1)
                ex, ey = random.randint(0, self.size-1), random.randint(0, self.size-1)
                # Ensure start and exit points are not the same and not blocked
                if (sx, sy) != (ex, ey) and self.maze[sx][sy] != '#' and self.maze[ex][ey] != '#':
                    break
            self.start = (sx, sy)
            self.exit = (ex, ey)
        else:
            # Use fixed start and exit points
            self.start = (0, 0)
            self.exit = (self.size-1, self.size-1)
            self.maze[0][0] = ' '
            self.maze[self.size-1][self.size-1] = ' '
        # Mark the start and exit points in the maze
        self.maze[self.start[0]][self.start[1]] = 'S'
        self.maze[self.exit[0]][self.exit[1]] = 'E'
        return self.maze, self.start, self.exit