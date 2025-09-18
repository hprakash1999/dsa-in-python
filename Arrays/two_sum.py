# Problem:  Find two numbers in the array that add up to a specific target.

def two_sum(nums, target):
    seen = {}   # number → index
    
    for i, n in enumerate(nums):
        diff = target - n
        print(f"Loop: {i}, Diffrence: {diff}")
        print(f"Seen before: {seen}")
        
        if diff in seen:
            print(f"Pair found! {diff}")
            return (seen[diff], i)   # return indices
        
        seen[n] = i   # store 
        print(f"Seen after: {seen}")
    
    return ()


print(two_sum([2, 5, 3, 9, 7], 11))