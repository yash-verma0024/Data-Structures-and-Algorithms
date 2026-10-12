class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        n = len(seq)
        depth = 1
        group = []
    
        for i in range(n):
            if seq[i] == "(":
                depth += 1
                group.append(depth % 2)
            else:
                group.append(depth % 2)
                depth -= 1
        return group