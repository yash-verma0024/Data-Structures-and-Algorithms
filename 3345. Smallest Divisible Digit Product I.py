class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            digit_product = 1
            temp = n
            while temp > 0:
                digit_product *= (temp % 10)
                temp //= 10

            if n == 0:
                digit_product = 0
                
            if digit_product % t == 0:
                return n
            
            n += 1
