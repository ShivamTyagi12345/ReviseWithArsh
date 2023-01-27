class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        primes = [True] * (right + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(right ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, right + 1, i):
                    primes[j] = False
        nums = [x for x in range(left, right + 1) if primes[x]]
        
        # print(nums)
        l = len(nums)
        res = []
        min_dif  = float('inf')
        for i in range(0, l-1):
            for j in range(i+1, l):
                dif = nums[j] - nums[i]
                if dif < min_dif:
                    res.append([nums[i], nums[j]])
                    min_dif = dif
                else:
                    break
        # print(res)
        if res:
            return res[-1]
        return [-1, -1]
        


