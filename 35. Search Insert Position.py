##########################################################################
#                         Brute Force Solution                           #
##########################################################################

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        for i in range(0,n-1):
            if nums[i] > target:
                return i


##########################################################################
#                        Binary Search Solution                          #
##########################################################################

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        idx = n 
        low, high = 0, n-1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                idx = mid
                high = mid - 1
            else:
                low = mid + 1

        return idx