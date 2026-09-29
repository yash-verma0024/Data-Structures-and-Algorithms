class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        result = []
        for i in range(1, n+1):
            if i > target[-1]:
                break
            if i in target:
                result.append("push")
            else:
                result.append("push")
                result.append("pop")
        return result