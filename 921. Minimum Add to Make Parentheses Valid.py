class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        n = len(s)
        open_paran = 0
        close_paran = 0
    
        for i in range(n):
            if s[i] == "(":
                open_paran += 1
            else:
                close_paran += 1
    
        return abs(open_paran-close_paran)