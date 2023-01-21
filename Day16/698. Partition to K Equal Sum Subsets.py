class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        vis = set()
        req = sum(nums) // k
        flag = True

        def knapsack(W, nums, index, vis):
            if index >= len(nums) or W < 0:
                return False
            if W == 0 :
                return True
            left , right = False, False
            if index not in vis:
                vis.add(index)
                left = knapsack( W-nums[index], nums, index+1, vis )
                vis.remove(index)
            right = knapsack(W, nums, index+1, vis)
            return left or right
            
            
        for i in range(k):
            if not knapsack(req, nums, 0, vis):
                return False
        return True




            

                                                                                                                                   
        
         