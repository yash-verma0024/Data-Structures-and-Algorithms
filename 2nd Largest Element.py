# # Method 1 : Brute force
# def second_largest(arr):
#     arr.sort()
#     return arr[-2]

# print(second_largest([-7,-88,-99,-8,-1]))

# # TC : O(nlogn)
# # SC : O(1)


# # Method 2 : Better approach
# def second_largest(nums):
#     largest = float("-inf")
#     s_largest = float("-inf")
#     n = len(nums)

#     for i in range(0,n):
#         largest = max(largest,nums[i])

#     for i in range(0,n):
#         if nums[i] > s_largest and nums[i] != largest:
#             s_largest = nums[i]
#     return s_largest

# # TC : O(2n)   --> O(n)
# # SC : O(1)


# # Method 3 : Optimal approach
# def second_largest(nums):
#     largest = float("-inf")
#     s_largest = float("-inf")
#     n = len(nums)

#     for i in range(0,n):
#         if nums[i] > largest:
#             s_largest = largest
#             largest = nums[i]
#         elif nums[i] > s_largest and nums[i] != largest:
#             s_largest = nums[i]
#     return s_largest

# # TC : O(n)
# # SC : O(1)