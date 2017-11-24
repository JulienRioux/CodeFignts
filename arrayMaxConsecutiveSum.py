# Given array of integers, find the maximal possible sum of some of its k consecutive elements.

# Example

# For inputArray = [2, 3, 5, 1, 6] and k = 2, the output should be
# arrayMaxConsecutiveSum(inputArray, k) = 8.
# All possible sums of 2 consecutive elements are:

# 2 + 3 = 5;
# 3 + 5 = 8;
# 5 + 1 = 6;
# 1 + 6 = 7.
# Thus, the answer is 8.

def arrayMaxConsecutiveSum(inputArray, k):
    # keep in memory the maximal Sum
    maxSum = sum(inputArray[0:k])
    # Copy in testSum the maxSum which is the first tested sum of the input array 
    testSum = maxSum
    # Iterate over the array (k at a time)
    for i in range(len(inputArray)-k):
        (
        # To avoid to make the sum of the element in the array at
        # each iteration; add the next element and substract the 
        # last element present in the last sum
        testSum += inputArray[i+k] - inputArray[i]
        # Check if the testSum is bigger than the maxSum up to date
        # If bigger, testSum is the new maxSum
        if testSum > maxSum:
                    maxSum = testSum
    
    return maxSum
