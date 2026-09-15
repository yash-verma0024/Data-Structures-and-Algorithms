##########################################################################
#                         Brute Force Solution                           #
##########################################################################

def search(nums: list[int], target: int) -> int:
    n = len(nums)

    # case 1 : target not in nums
    is_present = False
    for i in range(n):
        if nums[i] == target:
            is_present = True
            break

    if is_present == False:
        return -1

    # Case 2 : target is present in nums
    for j in range(n):
        if nums[j] == target:
            return j
    



##########################################################################
#                        Binary Search Solution                          #
##########################################################################

def search(nums: list[int], target: int) -> int:
    n = len(nums)
    ub, lb = -1,-1
    low,high = 0,n-1

    for i in range(n):
        mid = (low+high)//2
        if nums[mid] < target:
            lb


nums = [4,5,6,7,0,1,2]
target = 0
print(search(nums, target))