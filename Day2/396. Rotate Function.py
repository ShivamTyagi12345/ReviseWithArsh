class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        base, n, score = 0, len(nums), 0
        for i in range(n):
            score += i*nums[i]
        # print(res)
        ans = score
        x = sum(nums)

        for i in range(1, n):
            score = score - n*nums[n-i] + x
            # print(s)
            ans = max(ans, score)
        return ans

    
     
 