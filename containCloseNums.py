# Given an array of integers nums and an integer k, determine whether there are two distinct 
# indices i and j in the array where nums[i] = nums[j] and the absolute difference between 
# i and j is less than or equal to k.

# Example

# For nums = [0, 1, 2, 3, 5, 2] and k = 3, the output should be
# containsCloseNums(nums, k) = true.

# There are two 2s in nums, and the absolute difference between their positions is exactly 3.

# For nums = [0, 1, 2, 3, 5, 2] and k = 2, the output should be

# containsCloseNums(nums, k) = false.

# The absolute difference between the positions of the two 2s is 3, which is more than k.



def containsCloseNums(nums, k):
    # Return False if nums == 1 or 0
    if len(nums) < 2:
        return False
    # Create an empty dict to store the nums as keys and index as value
    D = {}
    # Append the key/value (number/index) element in the dictionnary
    for i in range(len(nums)):
        # Append it to D if there is the num isn't already there as key
        if nums[i] not in D:
            D[nums[i]] = i
        else:
            # If already there, check if the current index minus the index already there 
            if i - D[nums[i]] <= k:
                # Stop if it's the case
                return True
            else:
                # Otherwise, replace the index value by the current index
                D[nums[i]] = i
    
    return False
