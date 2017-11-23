#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Import permutation from intertools to make all the possibles rearangement of the inputArray
from itertools import permutations

def stringsRearrangement(inputArray):
    
    def listOfStringDiffByOneCharOnly(someArray):
        # Init the the number of consecutive string diff by one char only
        z = 0
        for i in range(len(someArray)-1):
            # Counter of difference of char between 2 consecutives strings
            c = 0
            # Iterate over every char in the string in comparaison
            for j in range(len(someArray[0])):
                # Check how many different char there is
                if someArray[i][j] != someArray[i+1][j]:
                    c += 1
            # If there is only one char of difference between the 2 consecutive strings 
            # in the array, add 1 to the number of consecutive string different by one char only
            if c == 1:
                z += 1
        # Check if there is only 1 different char between each strings of the list 
        return z == len(inputArray)-1
    
    # get all permutations of inputArray
    perm = permutations(inputArray)

    # For each possible permutation of the list, test if there is only 1 different 
    # char between each consecutives strings of the list
    for i in list(perm):
        # Stop when it found a possible way to rearrange the list
        if listOfStringDiffByOneCharOnly(list(i)) == True:
            return True
    # Return false if there is no way to rearange the list to get a viable solution
    return False



