Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with digits so that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid contains all of the digits from 1 to 9.

This algorithm should check if the given grid of numbers represents a correct solution to Sudoku.

Example

For the first example below, the output should be true. For the other grid, the output should be false: each of the nine 3 × 3 sub-grids should contain all of the digits from 1 to 9.


def sudoku(grid):
    
    # Check if each list contain the numbers 1 to 9
    def counter1To9(list):
        c = 1
        # Iterate over each element to see if it contain the 1 to 9 numbers
        for i in range(9):
            if list.count(c) != 1:
                return False
            c += 1
        return True
    
    # Check each row and column if they're legal
    for i in range(9):
        # Check for row
        if counter1To9(grid[i]) == False:
            return False
        # Check for column
        if counter1To9((list([grid[j][i] for j in range(9)]))) == False:
            return False

    # Check if all the 3by3 are legal matrix
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            # Create a list contain each of the nine threeBy3 matrix
            threeBy3 = grid[i][j:j+3] + grid[i+1][j:j+3] + grid[i+2][j:j+3]
            if counter1To9(threeBy3) == False:
                return False
    # If everythings is legal, this is a corect solution
    return True
