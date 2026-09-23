class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = []
        count = 0
        for i in range(n):
            element = nums[i]
            for j in range(n):
                if nums[j] < element:
                    count += 1
            result.append(count)
            count = 0
        return result