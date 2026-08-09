# Brute force Solution

nums = [5,9,1,2,4,15,6,3]

# def twoSum(nums, target):
#     n = len(nums)
#     for i in range(0,n-1):
#         for j in range(1, n):
#             if nums[i] + nums[j] == target:
#                 return [i,j]

# print(twoSum(nums,11))


# Optimal solution

def twoSum(nums, targets):
    n = len(nums)
    hash_map = {}
    for i in range(0,n):
        remaining = targets - nums[i]
        if remaining in hash_map:
            return [hash_map[remaining],i]
        hash_map[nums[i]] = i

print(twoSum(nums,11))