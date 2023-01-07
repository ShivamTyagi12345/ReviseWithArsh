class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        nums.sort()
        def gcd(x, y):
            while y:
                x, y = y, x%y
            return x
        hcf = numsDivide[0]
        for i in range(1, len(numsDivide)):
            hcf = gcd(hcf, numsDivide[i])
            
        print("hcf:", hcf)
        res = 0
        for num in nums:
            if hcf % num == 0:
                break
            res +=1
        if res == len(nums):
            return -1
        return res
