# This file provides a function to visualize the maze and the solution paths

# The maze is displayed as a grid with different colors for different elements:
# - Black cells represent walls (#)
# - Green cell represents the start (S)
# - Red cell represents the exit (E)
# - White cells represent open paths

# Solution paths for BFS, DFS, and A* are shown as dashed lines in different colors:
# - Purple for BFS
# - Orange for DFS
# - Cyan for A*

# Metrics like path cost, nodes expanded, execution time, and memory usage are displayed below the maze

import matplotlib.pyplot as plt
import numpy as np

def plot_maze(maze, paths=None, metrics=None):
    size = len(maze)
    # Set a light gray background to distinguish from white maze cells
    _, ax = plt.subplots(figsize=(8,8), facecolor='#eaeaea')
    # Create a blank image to represent the maze
    img = np.ones((size, size, 3), dtype=np.float32)
    # Loop through each cell in the maze to set its color
    for i in range(size):
        for j in range(size):
            # Set black color for walls
            if maze[i][j] == '#':
                img[i, j] = [0, 0, 0]
            # Set green color for the start point
            elif maze[i][j] == 'S':
                img[i, j] = [0, 1, 0]
            # Set red color for the exit point
            elif maze[i][j] == 'E':
                img[i, j] = [1, 0, 0]
    # Display the maze image
    ax.imshow(img, origin='lower', extent=[0, size, 0, size])
    # Draw grid lines to separate cells
    for x in range(size+1):
        ax.axhline(x, color='gray', linewidth=0.5, zorder=2)
        ax.axvline(x, color='gray', linewidth=0.5, zorder=2)
    # Overlay solution paths on the maze
    color_map = {'bfs': 'purple', 'dfs': 'orange', 'astar': 'cyan'}
    path_order = ['bfs', 'astar', 'dfs']  # Plot DFS last
    if paths:
        for name in path_order:
            path = paths.get(name)
            if path and len(path) > 1:
                # Extract x and y coordinates from the path
                x, y = zip(*path)
                lw = 2  # Default line width for BFS and DFS
                if name == 'astar':
                    lw = 4  # Thicker line for A*
                # Plot the path with a dashed line
                ax.plot([j+0.5 for j in y], [i+0.5 for i in x], color=color_map.get(name, 'black'), linestyle='--', linewidth=lw, label=name.upper())
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(0, size)
    ax.set_ylim(0, size)
    ax.set_facecolor('#eaeaea')
    ax.legend()
    # Annotate metrics with higher precision for time
    if metrics:
        y = -1.5
        for name, m in metrics.items():
            # Show time in ms with 2 decimals, or in μs if < 1 ms
            if m['time'] >= 1:
                time_str = f"{m['time']:.2f} ms"
            else:
                time_str = f"{m['time']*1000:.0f} μs"
            ax.text(0, y, f"{name.upper()}: Cost={m['cost']} Nodes={m['nodes']} Time={time_str} MaxMem={m['mem']}", color=color_map.get(name, 'black'), fontsize=10)
            y -= 1
    plt.tight_layout()
    plt.show()
