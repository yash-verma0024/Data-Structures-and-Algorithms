class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        num = []
        for i in range(len(nums)):
            num.append((nums[i])**2)
    
        num.sort()
        n = len(num)
        pos_num = num[:n//2]
        neg_num = num[n//2:]
    
        return sum(neg_num) - sum(pos_num)