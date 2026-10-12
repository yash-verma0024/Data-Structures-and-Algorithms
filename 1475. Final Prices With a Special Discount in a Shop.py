class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        n = len(prices)
        result = prices.copy()
    
        for i in range(n-2):
            for j in range(i+1, n-1):
                if prices[i] >= prices[j]:
                    value = prices[i] - prices[j]
                    result[i] = value
                    break
                
        return result