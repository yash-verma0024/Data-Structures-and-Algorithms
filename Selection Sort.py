# Selection sort in ascending order
def sel_sort(nums):
    n = len(nums)

    for i in range(0, n):
        min_idx = i
        for j in range(i+1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]

    return nums
print(sel_sort([5,4,3,2,1]))


# Selection sort in descending order
def sel_sort(nums):
    n = len(nums)

    for i in range(0, n):
        min_idx = i
        for j in range(i+1, n):
            if nums[j] > nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]

    return nums

print(sel_sort([1,2,3,4,5]))


# TC : O([N(N+1)]/2)  --> O(N^2)
# SC : O(1)