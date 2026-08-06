class Solution:
    def climbStairs(self, n: int) -> int:
        # If there are 1, 2, or 3 steps, the number of ways is equal to n
        if n <= 3:
            return n
        # Keep track of the ways to reach the previous two steps
        prev_1 = 3   # ways to reach step 3
        prev_2 = 2   # ways to reach step 2
        current = 0

        # Build up the answer from step 4 all the new to n
        for i in range(4, n+1):
            current = prev_1 + prev_2
            prev_2 = prev_1
            prev_1 = current
        
        return current