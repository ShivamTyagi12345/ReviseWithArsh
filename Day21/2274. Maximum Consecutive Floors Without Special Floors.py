class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        count, res = 0, 0
        special.sort()

        for i in range(bottom, top+1):
            if i not in special:
                count +=1
                res = max(res, count)
            else:
                count = 0
        return res
        