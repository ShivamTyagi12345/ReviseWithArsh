# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, nums: 'MountainArray') -> int:
        left = 0
        right = nums.length()-1
        mid1, mid2 =  0, 0 
        while(left < right):
            mid1 = (left + right) // 2
            mid2 = mid1 + 1
            if nums.get(mid1) < nums.get(mid2):
                left = mid2
            else:
                right = mid1
        # Now that left has index of Peak

        def binary(s, e):
            if s > e : return -1
            mid = s + (e - s )// 2

            if target ==  nums.get(mid): 
                return mid
            elif target < nums.get(mid):
                return binary(s, mid-1)
            else:
                return binary(mid+1, e)
            
        A = binary(0, left)
        print(A)
        B = binary(left, nums.length()-1)
        print(B)

        if A== -1 and B!= -1:
            return B
        if A != -1 and B == -1:
            return A

        return min(A, B)


            
            
        