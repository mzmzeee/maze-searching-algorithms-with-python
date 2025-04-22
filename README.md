# Maze Solving Assignment (EC558 Assignment)

## Overview
This assignment implements BFS, DFS, and A* search algorithms to solve a randomly generated 25x25 maze. The assignment visualizes the maze and the solution paths, and compares the algorithms based on path cost, nodes expanded, execution time, and memory usage.

## Features
- Maze generation with random or fixed start/end
- BFS, DFS, and A* search algorithms
- Visualization of maze, solution paths (dashed lines), and metrics
- All results are shown on the figure for clarity

## File Structure
```
assignment/
├── src/
│   ├── maze.py          # Maze generation
│   ├── algorithms.py    # BFS, DFS, A* implementations
│   ├── visualize.py     # Visualization of maze and paths
│   └── main.py          # Entry point for testing and comparisons
├── requirements.txt     # Dependencies
└── README.md            # This file
```

## Requirements
- Python 3.8+
- matplotlib==3.7.1
- numpy==1.24.3

Install dependencies with:
```
pip install -r requirements.txt
```

## How to Run
From the assignment root, run:
- to activate the environment run the following command in any bash terminal or linux environment:
  ```
  source .venv/bin/activate
  ```
- For fixed start (0,0) and exit (24,24):
  ```
  python3 src/main.py --fixed
  ```
- For random start and exit:
  ```
  python3 src/main.py --random
  ```
- to repeat the algorithms multiple time on the generated maze use:
  ```
  python3 src/main.py --repeat (number of times ex:1000)
  ``` 
  A figure will appear showing the maze, solution paths for each algorithm (BFS: purple, DFS: yellow, A*: cyan)(green block is the start and the red block is the exit), and metrics (cost, nodes, time, memory) for each algorithm.

  close the figure so that the process terminates 

- to deactivate the environment:
  ```
  deactivate
  ```

## Analysis and Comparison of Search Methods

The implemented search algorithms—BFS, DFS, and A*—were compared using the following criteria:

- **Memory Requirement**: Measured as the maximum length of the queue (or stack) used during the search.
- **Time Requirement**: Measured as the total number of nodes (positions) checked/expanded during the search.
- **Solution Optimality**: Measured as the cost (length) of the generated solution path.

### Summary of Results

- **Breadth-First Search (BFS)**
  - **Memory**: Uses a queue; memory usage can be high for large mazes, as all frontier nodes are stored.
  - **Time**: Explores all nodes at each depth level; can be slow for deep solutions.
  - **Optimality**: Always finds the shortest path (optimal solution) in an unweighted maze.

- **Depth-First Search (DFS)**
  - **Memory**: Uses a stack; generally lower memory usage than BFS, but can be high if the path is long or the maze is complex.
  - **Time**: May check many unnecessary nodes, especially in large or complex mazes.
  - **Optimality**: Does not guarantee the shortest path; may return suboptimal solutions.

- **A* Search**
  - **Memory**: Uses a priority queue; memory usage depends on the heuristic and maze structure, but is often more efficient than BFS for finding optimal paths.
  - **Time**: Typically faster than BFS and DFS when a good heuristic is used, as it prioritizes promising paths.
  - **Optimality**: Finds the shortest path if the heuristic is admissible (as in this implementation).

## Heuristic Function Justification for A* Search

For the A* search algorithm, the heuristic function used is the **Manhattan distance** between the current node and the goal node. The Manhattan distance is calculated as:

    h(n) = |x1 - x2| + |y1 - y2|

where (x1, y1) is the current node and (x2, y2) is the goal node.

**Justification:**
- The Manhattan distance is appropriate for grid-based mazes where movement is restricted to four directions (up, down, left, right), and diagonal movement is not allowed.
- It is **admissible** (never overestimates the true cost) and **consistent**, ensuring that A* will always find the optimal path if one exists.
- It provides a good estimate of the minimum number of steps required to reach the goal, making the search efficient by prioritizing nodes closer to the goal.

This choice of heuristic balances optimality and efficiency for the maze-solving problem in this assignment.

### Conclusions
- **BFS** is reliable for finding optimal solutions but can be slow and memory-intensive for large mazes.
- **DFS** is fast and memory-efficient in some cases but does not guarantee optimal solutions.
- **A*** combines the strengths of both, offering optimal solutions with improved efficiency when using an appropriate heuristic (here, the Manhattan distance).

All metrics (cost, nodes expanded, time, memory) are displayed in the visualization for each run, allowing for direct comparison between the algorithms.

## Author
- Motaz M Alharbi 
- EC558 Assignment1, 2025
