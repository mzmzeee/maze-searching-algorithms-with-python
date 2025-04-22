# This file contains the implementation of three maze-solving algorithms: BFS, DFS, and A*

# BFS: Breadth-First Search algorithm
# It explores all possible paths level by level to find the shortest path
# Uses a queue to keep track of nodes to visit next
# Tracks visited nodes to avoid revisiting them
# Keeps track of the parent of each node to reconstruct the path

# DFS: Depth-First Search algorithm
# It explores as far as possible along each branch before backtracking
# Uses a stack to keep track of nodes to visit next
# Tracks visited nodes to avoid revisiting them
# Keeps track of the parent of each node to reconstruct the path

# A*: A-star Search algorithm
# It uses a heuristic (Manhattan distance) to prioritize nodes closer to the goal
# Uses a priority queue to keep track of nodes to visit next
# Tracks visited nodes to avoid revisiting them
# Keeps track of the parent of each node to reconstruct the path
# Calculates tentative g-score for each neighbor as g-score of current node + 1
from collections import deque
import heapq

def bfs(maze, start, exit):
    # Initialize the queue with the start node
    queue = deque([start])
    # Keep track of visited nodes to avoid revisiting them
    visited = set([start])
    # Dictionary to store the parent of each node for path reconstruction
    parent = {start: None}
    # Counter for the number of nodes expanded during the search
    nodes_expanded = 0
    # Variable to track the maximum memory usage during the search
    max_memory = 1

    while queue:
        # Update the maximum memory usage
        max_memory = max(max_memory, len(queue))
        # Remove the first node from the queue
        node = queue.popleft()
        # Increment the count of nodes expanded
        nodes_expanded += 1
        # Check if the current node is the exit
        if node == exit:
            break
        # Explore all possible neighbors of the current node
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = node[0]+dx, node[1]+dy
            # Check if the neighbor is within bounds and not a wall
            if 0<=nx<len(maze) and 0<=ny<len(maze) and maze[nx][ny] != '#' and (nx,ny) not in visited:
                # Add the neighbor to the queue
                queue.append((nx,ny))
                # Mark the neighbor as visited
                visited.add((nx,ny))
                # Set the current node as the parent of the neighbor
                parent[(nx,ny)] = node

    path = []
    if exit in parent:
        node = exit
        while node:
            path.append(node)
            node = parent[node]
        path.reverse()
    return path, nodes_expanded, max_memory

def dfs(maze, start, exit):
    # Initialize the stack with the start node using deque for efficiency
    stack = deque([start])
    # Keep track of visited nodes to avoid revisiting them
    visited = set([start])
    # Dictionary to store the parent of each node for path reconstruction
    parent = {start: None}
    # Counter for the number of nodes expanded during the search
    nodes_expanded = 0
    # Variable to track the maximum memory usage during the search
    max_memory = 1

    while stack:
        # Update the maximum memory usage
        max_memory = max(max_memory, len(stack))
        # Remove the last node from the stack (LIFO)
        node = stack.pop()
        # Increment the count of nodes expanded
        nodes_expanded += 1
        # Check if the current node is the exit
        if node == exit:
            break
        # Explore all possible neighbors of the current node
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = node[0]+dx, node[1]+dy
            # Check if the neighbor is within bounds and not a wall
            if 0<=nx<len(maze) and 0<=ny<len(maze) and maze[nx][ny] != '#' and (nx,ny) not in visited:
                # Add the neighbor to the stack
                stack.append((nx,ny))
                # Mark the neighbor as visited
                visited.add((nx,ny))
                # Set the current node as the parent of the neighbor
                parent[(nx,ny)] = node
    path = []
    if exit in parent:
        node = exit
        while node:
            path.append(node)
            node = parent[node]
        path.reverse()
    return path, nodes_expanded, max_memory

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(maze, start, exit):
    # Initialize the g-score dictionary with the start node having a score of 0
    g_score = {start: 0}
    # Priority queue to store nodes to visit, starting with the start node
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, exit), 0, start))
    # Dictionary to keep track of the parent of each node for path reconstruction
    parent = {start: None}
    # Set to keep track of visited nodes
    visited = set()
    # Variable to count the number of nodes expanded during the search
    nodes_expanded = 0
    # Variable to track the maximum memory usage during the search
    max_memory = 1

    while open_set:
        # Update the maximum memory usage
        max_memory = max(max_memory, len(open_set))
        # Pop the node with the lowest f-score from the priority queue
        _ , cost , node = heapq.heappop(open_set)
        # Skip the node if it has already been visited
        if node in visited:
            continue
        # Mark the node as visited
        visited.add(node)
        # Increment the count of nodes expanded
        nodes_expanded += 1
        # Check if the current node is the exit
        if node == exit:
            break
        # Explore all possible neighbors of the current node
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = node[0]+dx, node[1]+dy
            neighbor = (nx, ny)
            # Check if the neighbor is within bounds and not a wall
            if 0<=nx<len(maze) and 0<=ny<len(maze) and maze[nx][ny] != '#':
                # Calculate the tentative g-score for the neighbor
                tentative_g = g_score[node] + 1
                # Update the g-score and parent if the new g-score is better
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    g_score[neighbor] = tentative_g
                    # Calculate the f-score and add the neighbor to the priority queue
                    f = tentative_g + heuristic(neighbor, exit)
                    heapq.heappush(open_set, (f, tentative_g, neighbor))
                    parent[neighbor] = node

    path = []
    if exit in parent:
        node = exit
        while node:
            path.append(node)
            node = parent[node]
        path.reverse()
    return path, nodes_expanded, max_memory
