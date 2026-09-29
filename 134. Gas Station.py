class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        n= len(gas)
        current_idx=0
        total_gas=0
        
        if sum(gas)<sum(cost):
            return -1
            
        for i in range(n):
            total_gas += gas[i] - cost[i]
            if total_gas < 0:
                current_idx =i + 1
                total_gas=0
        return current_idx