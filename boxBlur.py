#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def boxBlur(image):
    # I keep the totalRow and totalColumn to know when stop the iterations
    totalRow = len(image)
    totalColumn = len(image[0])
    # Initialize the row and column variable for the iterations
    row = 0
    column = 0
    # Init the value of the middlepixel to 0
    middlePixel = 0
    # Init the final list which will be a matrix of middlePixel
    finalList = []
    
    # Iterate over the row (3 at the time) until the end
    while row <= totalRow-3:
        # Initialize a tempList to put the middlePixel of the same 3x row
        # before put them in the finalList 
        tempList = []
        # iterate over the column (3 at the time) until the end
        while column <= totalColumn-3:
            # sum the 3x3 value matrix
            middlePixel += sum(image[row][column:column+3])
            middlePixel += sum(image[row+1][column:column+3])
            middlePixel += sum(image[row+2][column:column+3])
            # put the middlePixel value in the temp list
            tempList.append(middlePixel//9)
            # Re-init the middlePixel for the next 3x3 block
            middlePixel = 0
            # Change of column 
            column += 1
        # When we have all the middlePixel value for a 3x row,
        # add the list of middlePixel to the final list
        # of middlePixels
        finalList.append(tempList)
        # Re-init the column to 0 when we change of row
        column = 0
        # change of row (3 at the time...)
        row += 1
    
    return finalList


