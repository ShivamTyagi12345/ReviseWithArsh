class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = [i for i in range(1, n+1)]
        k = k-1
        def helper(nums, position ):
            if len(nums)==1:
                return  nums[0]
            position = (position + k) % len(nums)  
            print(nums, position)
            nums.remove(nums[position])
            return helper(nums, position)
        return helper(nums, 0)

        