# Intuition / Approach
# Identify Positions:
# The bot starts in the center of the grid.
# The princess is located at one of the four corners.
# Calculate Moves:
# Determine the difference in row and column indices between the bot and the princess.
# Generate the necessary moves (UP, DOWN, LEFT, RIGHT) based on these differences.
# Output Moves:
# Print the moves in the required format.
# Variables
# bot_pos: The position of the bot, which is always the center of the grid (n // 2, n // 2).
# princess_pos: The position of the princess found using list comprehension.
# vertical_moves: The string containing all vertical moves.
# horizontal_moves: The string containing all horizontal moves.
# Complexity
# Time Complexity: O(1)
# Identifying the bot and princess positions is constant time as it only involves checking fixed positions (four corners).
# Calculating and printing moves involves simple arithmetic and string operations.
# Space Complexity: O(N^2)
# The space used to store the grid is proportional to the size of the grid.
#!/usr/bin/python

def displayPathtoPrincess(n,grid):
#print all the moves here
    # Find the position of the bot 'm'
    bot_pos = (n // 2, n // 2)
    
    # Find the position of the princess 'p'
    princess_pos = [(i, j) for i in [0, n-1] for j in [0, n-1] if grid[i][j] == 'p'][0]
    
    # Calculate the moves
    vertical_moves = 'DOWN\n' * (princess_pos[0] - bot_pos[0]) + 'UP\n' * (bot_pos[0] - princess_pos[0])
    horizontal_moves = 'RIGHT\n' * (princess_pos[1] - bot_pos[1]) + 'LEFT\n' * (bot_pos[1] - princess_pos[1])
    
    # Print the moves
    print(vertical_moves + horizontal_moves, end='')

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)