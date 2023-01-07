class Solution:
    def trailingZeroes(self, n: int) -> int:
        prod = 1
        for i in range(1, n+1):
            prod *= i
        res = 0
        while prod > 0:
            d =  prod %10
            if d != 0:
                break
            res +=1
            prod //=10
        return res