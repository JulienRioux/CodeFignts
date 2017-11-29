# Given an array of integers nums and an integer k, determine whether there are two distinct indices i and j in the array where nums[i] = nums[j] and the absolute difference between i and j is less than or equal to k.

# Example

# For nums = [0, 1, 2, 3, 5, 2] and k = 3, the output should be
# containsCloseNums(nums, k) = true.

# There are two 2s in nums, and the absolute difference between their positions is exactly 3.

# For nums = [0, 1, 2, 3, 5, 2] and k = 2, the output should be

# containsCloseNums(nums, k) = false.

# The absolute difference between the positions of the two 2s is 3, which is more than k.




def containsCloseNums(nums, k):
    
    if len(nums) < 2:
        return False
    
    D = {}
    
    ans = False
    
    for i in range(len(nums)):
        if nums[i] not in D:
            D[nums[i]] = i
        else:
            if type(D[nums[i]]) == int:
                if i - D[nums[i]] <= k:
                    ans = True
                else:
                    D[nums[i]] = [D[nums[i]]]
                    D[nums[i]].append(i)
            else:
                for index in D[nums[i]]:
                    print(i, index)
                    if i - index <= k:
                        ans = True
    
    return ans
