class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first, sec = float('inf'), float('inf')
        for item in nums:
            if item <= first:
                first  = item
            elif item  <= sec:
                sec = item
            else:
                return True
        return False
        