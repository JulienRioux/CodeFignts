



def arrayMaxConsecutiveSum(inputArray, k):
    
    maxSum = sum(inputArray[0:k])
    testSum = maxSum
    
    for i in range(len(inputArray)-k):
        testSum += inputArray[i+k] 
        testSum -=  inputArray[i]
        lastSum = testSum
        if testSum > maxSum:
                    maxSum = testSum
    
    return maxSum
