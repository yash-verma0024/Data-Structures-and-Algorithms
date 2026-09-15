##########################################################################
#                         Brute Force Solution                           #
##########################################################################

def search(nums: list[int], target: int) -> int:
    n = len(nums)

    for i in range(n):
        if nums[i] == target:
            return i
    return -1


##########################################################################
#                        Binary Search Solution                          #
##########################################################################

def search(nums: list[int], target: int) -> int:
    n = len(nums)
    low,high = 0,n-1
    while low <= high:
        mid = (low + high)//2
        if nums[mid] == target:
            return mid
        if nums[mid] <= nums[high]:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if nums[low] <= target <= nums[high]:
                high = mid - 1
            else:
                low = mid + 1

    return -1

nums = [4,5,6,7,0,1,2]
target = 1
print(search(nums, target))