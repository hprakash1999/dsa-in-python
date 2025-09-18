# Problem: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

def two_sum(nums, target):
    seen = {}   # number -> index
    
    for i, n in enumerate(nums):
        diff = target - n
        
        if diff in seen:
            return [seen[diff], i]   # return indices
        
        seen[n] = i   # store 
    
    return []


print(two_sum([2, 5, 3, 9, 7], 11))