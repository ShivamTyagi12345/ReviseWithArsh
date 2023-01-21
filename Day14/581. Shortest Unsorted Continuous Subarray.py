class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        leftmost, rightmost= len(nums), 0 
        arr = sorted(nums)
        if arr == nums:
            return 0
        for i in range(len(nums)):
            if nums[i]!=arr[i]:
                leftmost = min(leftmost, i)
                
                rightmost = max(rightmost, i)
        print(leftmost, rightmost)
                

        
        return rightmost-leftmost+1
                
                      