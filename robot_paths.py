#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def count_paths(input_string):
    split_string = input_string.strip().split('\n')#creates a list that contains substrings of the input string. Each substring contains characters on the same line. Trailing spaces are also removed
    string_grid = [split_again.split() for split_again in split_string]# creates a 2D grid of the characters in the string
    grid = string_grid
    rows = len(grid)#Determines the number of rows in the grid
    cols = len(grid[0])#computes the number of columns in the grid
    #creates a new variable that will hold users's input
    user_interface = None
    #If condition checks if the grid contains more cells than a 10 by 10 rectangular grid
    if ((rows * cols > 100)):
        print("Alert!!!Grid is larger than 10 by 10, the code will take a very long time to run")
        #user_interface collects user input
        user_interface = input("Type exactly 'Continue' to proceed nevertherless or 'Stop' to terminate operation").strip()#Removes trailing spaces from user_input
        #Checks if user entered "Stop' and terminates operation
    if user_interface == 'Stop':
        print("Search operation terminated")
        #checks if user entered 'continue' or if the number of cells in the grid is less than or equal to 100
    elif (user_interface == 'Continue') or ((rows * cols) <= 100):
        #target_pathcells is the total number of non-blocked cells that the robot should visit exactly once
        target_pathcells_init = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] not in ['X', 'x']:
                    target_pathcells_init += 1
        target_pathcells = target_pathcells_init
        legal_moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]#list contain the legal directions which the robot can move. These are right, left, up and down respectively
        #Replaces all cells in the grid with 'u'.'u' means unvisited
        grid = [['u' if (cell != 'X' and cell != 'x') else cell for cell in rows] for rows in grid]
        grid[0][0] ='v'# marks the starting point of the robot as 'v' -visited.
        #Initialized to zero, the variable path_counter counts the required total number of ways in wich the robot can move from A to B
        path_counter = 0
        #the recursively_bactrack functions carries out depth first search.
        def recursively_backtrack(y, z, cur_pathcells):
            nonlocal path_counter
            J = bool((y == (rows - 1)) and (z == (cols - 1)) and (cur_pathcells == target_pathcells))
            #checks if the robot is at the at the destination point B, and if the robot has not visited all cells
            if ((y == (rows - 1)) and (z == (cols - 1)) and (cur_pathcells != target_pathcells)):
                return 0
                #checks if the the robot is at the destination cell and if the robot has visited all cells in the grid
            if (J == True):
                path_counter += 1
                return 1
                #loops through all legal moves
            for move in range((len(legal_moves))):
                #calculates the new position of the robot based on some choice of moves
                ny_position, nz_position = y + legal_moves[move][0], z + legal_moves[move][1]
                #checks if the new position is within the grid, and also if it is not blocked or visited already
                if (0 <= ny_position <= (rows -1)) and (0 <= nz_position <= (cols -1))and (grid[ny_position][nz_position] not in ['X', 'x', 'v']):
                    #marks the new position as visited
                    grid[ny_position][nz_position] = 'v'
                    #recursive call
                    recursively_backtrack(ny_position, nz_position, cur_pathcells + 1)
                    #backtracks after reaching a dead end, marks position as unvisited
                    grid[ny_position][nz_position] = 'u'
        recursively_backtrack(0, 0, 1)
        return (path_counter)
        
# put the test case here
