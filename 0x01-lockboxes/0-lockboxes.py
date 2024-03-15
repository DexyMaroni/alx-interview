#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked.

    Args:
    - boxes (list of lists): A list of lists representing the boxes and their keys.

    Returns:
    - bool: True if all boxes can be unlocked, False otherwise.
    """

    # Get the total number of boxes
    n = len(boxes)

    # Initialize a list to keep track of visited boxes
    visited = [False] * n

    # Start DFS from box 0
    stack = [0]

    # Depth-First Search (DFS) algorithm
    while stack:
        # Pop a box from the stack
        box = stack.pop()
        
        # Mark the box as visited
        visited[box] = True

        # Iterate over the keys in the current box
        for key in boxes[box]:
            # If the key leads to an unvisited box, add it to the stack
            if not visited[key]:
                stack.append(key)

    # Check if all boxes have been visited
    return all(visited)
