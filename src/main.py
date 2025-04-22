# This file is the main entry point for running and comparing the maze-solving algorithms

# The time_algorithm function measures the average execution time of an algorithm
# It runs the algorithm multiple times and calculates the average time in milliseconds

# The run_all function runs all three algorithms (BFS, DFS, A*) on the same maze
# It collects the results (path cost, nodes expanded, execution time, memory usage) for each algorithm

# The main function does the following:
# 1. Parses command-line arguments to determine whether to use fixed or random start/exit points
# 2. Generates a maze using the Maze class
# 3. Runs all algorithms on the generated maze
# 4. Visualizes the maze, solution paths, and metrics using the plot_maze function

import argparse
from maze import Maze
from algorithms import bfs, dfs, astar
from visualize import plot_maze

def time_algorithm(algo, maze, start, exit, repeat=1000):
    import time
    total_time = 0
    last_result = None
    for _ in range(repeat):
        maze_copy = [row[:] for row in maze]
        t0 = time.perf_counter_ns()
        result = algo(maze_copy, start, exit)
        t1 = time.perf_counter_ns()
        total_time += (t1 - t0)
        last_result = result
    avg_time_ms = total_time / repeat / 1_000_000
    return *last_result, avg_time_ms

def run_all(maze_obj, maze, start, exit, repeat=1000):
    results = {}
    paths = {}
    # BFS
    path, nodes, mem, avg_time = time_algorithm(bfs, maze, start, exit, repeat)
    results['bfs'] = {'cost': len(path) if path else -1, 'nodes': nodes, 'time': avg_time, 'mem': mem}
    paths['bfs'] = path
    # DFS
    path, nodes, mem, avg_time = time_algorithm(dfs, maze, start, exit, repeat)
    results['dfs'] = {'cost': len(path) if path else -1, 'nodes': nodes, 'time': avg_time, 'mem': mem}
    paths['dfs'] = path
    # A*
    path, nodes, mem, avg_time = time_algorithm(astar, maze, start, exit, repeat)
    results['astar'] = {'cost': len(path) if path else -1, 'nodes': nodes, 'time': avg_time, 'mem': mem}
    paths['astar'] = path
    return results, paths

def main():
    # Parse command-line arguments to determine the maze configuration
    parser = argparse.ArgumentParser()
    parser.add_argument('--fixed', action='store_true', help='Use fixed start (0,0) and exit (24,24)')
    parser.add_argument('--random', action='store_true', help='Use random start and exit')
    parser.add_argument('--repeat', type=int, default=1000, help='Number of repetitions for timing (default: 1000)')
    args = parser.parse_args()

    # Create a Maze object
    maze_obj = Maze()
    # Generate the maze based on the command-line arguments
    if args.fixed:
        # Generate a maze with fixed start and exit points
        maze, start, exit = maze_obj.generate_maze(random_start_end=False)
    else:
        # Generate a maze with random start and exit points
        maze, start, exit = maze_obj.generate_maze(random_start_end=True)

    # Run all algorithms on the generated maze
    results, paths = run_all(maze_obj, maze, start, exit, repeat=args.repeat)

    # Visualize the maze, solution paths, and metrics
    plot_maze(maze, paths=paths, metrics=results)

if __name__ == '__main__':
    main()