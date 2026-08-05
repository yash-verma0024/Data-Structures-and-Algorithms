def sort(nums):
    n = len(nums)
    for i in range(n-2, -1, -1):
        is_swap = False
        for j in range(i+1):
            if nums[j] > nums[j+1]:                    # Change the comparison operator to '>' for ascending order
                nums[j], nums[j+1] = nums[j+1], nums[j]
                is_swap = True
        if is_swap == False:
            break
    return nums

print(sort([5, 1, 4, 2, 8]))


# TC : 
# in worst/avg case : O([N(N+1)]/2)   --> O(N^2)
# in best case : O(N)  --> when the array is already sorted

# SC : O(1)