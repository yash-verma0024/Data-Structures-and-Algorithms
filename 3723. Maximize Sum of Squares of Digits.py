class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        
        num_nines = sum // 9
        remainder = sum % 9
        
        digits = ['9'] * num_nines
        
        if remainder > 0:
            digits.append(str(remainder))
        
        zeros_needed = num - len(digits)
        digits.extend(['0'] * zeros_needed)
        
        return "".join(digits)
