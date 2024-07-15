# Intuition / Approach
# Identify Positions:
# The bot's position (r, c) is given.
# Find the princess's position in the grid.
# Calculate Move:
# Determine the difference in rows and columns between the bot and princess.
# Decide the next move (UP, DOWN, LEFT, RIGHT) based on these differences.
# Output Move:
# Print the determined move.
# Variables
# princess_pos: Position of the princess found by scanning the grid.
# row_diff: Difference between the bot's row and the princess's row.
# col_diff: Difference between the bot's column and the princess's column.
# Complexity
# Time Complexity: O(N^2)
# Finding the princess involves scanning the entire grid.
# Determining the move is done in constant time.
# Space Complexity: O(1)
# Only a few extra variables are used.
#!/usr/bin/python

def nextMove(n, r, c, grid):
    # Find princess's position
    princess_pos = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 'p'][0]
    
    # Calculate row and column differences
    row_diff = princess_pos[0] - r
    col_diff = princess_pos[1] - c
    
    # Determine the next move
    if row_diff > 0:
        return "DOWN"
    elif row_diff < 0:
        return "UP"
    elif col_diff > 0:
        return "RIGHT"
    elif col_diff < 0:
        return "LEFT"

# Read input
n = int(input())
r, c = [int(i) for i in input().strip().split()]
grid = [input().strip() for _ in range(n)]

# Output the next move
print(nextMove(n, r, c, grid))
