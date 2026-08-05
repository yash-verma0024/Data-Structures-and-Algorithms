# # Brute force solution

# def longestConsecutive(nums:list[int]) -> int:
#         n = len(nums)
#         max_count = 0
#         for i in range (0,n):
#                 num = nums[i]
#                 count = 1
#                 while num+1 in nums:
#                         count += 1
#                         num += 1
#                 max_count = max(max_count, count)
#         return max_count


# Optimal solution

def longestConsecutive(nums:list[int]) -> int:
    nums.sort()
    n = len(nums)
    count = 0
    last_smaller = float("-inf")
    longest = 0
    for i in range(0,n):
        num = nums[i]
        if num - 1 == last_smaller:
            count += 1
            last_smaller=num
        elif num != last_smaller:
            count = 1
            last_smaller = num

        longest = max(longest, count)
    return longest
            
nums = [0,3,7,2,5,8,4,6,0,1]
print(longestConsecutive(nums))