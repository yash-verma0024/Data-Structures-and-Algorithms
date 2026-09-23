class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        n = len(nums)
        one_occur = 0
        max_one_occur = 0

        if 0 not in nums:
            return len(nums)

        for i in range(n):
            if nums[i] == 1:
                one_occur += 1
            elif nums[i] == 0:
                if one_occur > max_one_occur:
                    max_one_occur = one_occur
                    one_occur = 0

        return max(one_occur, max_one_occur)