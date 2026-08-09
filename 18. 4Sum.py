##########################################################
#                Brute Force Solution                    #
##########################################################

from typing import List

# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         n = len(nums)
#         nums.sort()
#         my_set = set()

#         for i in range(0,n):
#             for j in range(i+1, n):
#                 for k in range(j+1, n):
#                     for l in range(k+1, n):
#                         if nums[i] + nums[j] + nums[k] + nums[l] == target:
#                             my_set.add(tuple([nums[i] , nums[j] , nums[k] , nums[l]]))

#         return my_set


##########################################################
#                   Better Solution                      #
##########################################################

# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         n = len(nums)
#         my_set = set()

#         for i in range(0,n):
#             for j in range(i+1, n):
#                 hash_set = set()
#                 for k in range(j+1, n):
#                     fourth = target - (nums[i] + nums[j] + nums[k])
#                     if fourth in hash_set:
#                         t = [nums[i] , nums[j] , nums[k] , fourth]
#                         t.sort()
#                         my_set.add(tuple(t))
#                     hash_set.add(nums[k])

#         result = []
#         for ans in my_set:
#             result.append(ans)
#         return result


##########################################################
#                  Optimal Solution                      #
##########################################################

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = []
        nums.sort()  
        
        for i in range(0, n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                k = j + 1
                l = n - 1
                
                while k < l:
                    total = nums[i] + nums[j] + nums[k] + nums[l]
                    
                    if total == target:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1
                            
                    elif total < target:
                        k += 1
                    else:
                        l -= 1
                        
        return ans
