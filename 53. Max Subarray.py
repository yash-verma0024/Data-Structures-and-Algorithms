# Brute Force Solution

nums = [-2,1,-3,4,-1,2,1,-5,4]

def maxSubarray(nums):
    n = len(nums)
    maxi = float("-inf")
    for i in range(0,n):
        total = 0
        for j in range(0,n):
            total = total + nums[j]
            maxi = max(maxi, total)
    return maxi

print(maxSubarray(nums))


# Optimal Solution

####################################################
#                 Kadane Algorithm                 #
####################################################

def maxSubarray(nums):
    n = len(nums)
    maxi = float("-inf")
    total = 0
    for i in range(0,n):
        total = total + nums[i]
        maxi = max(maxi, total)
        if total < 0:
            total = 0
    return maxi