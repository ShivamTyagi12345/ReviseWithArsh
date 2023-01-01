class Solution:
    def combinationSum3(self, k: int, target: int) -> List[List[int]]:
        res = []
        nums = [num for num in range(10)] 
        def dfs(curr, s, index):
            if s > target:
                return
            if s == target and len(curr)==k and 0 not in curr:
                res.append(curr)
                # print(curr, res)
                return
        
            for i in range(index, 10):
                dfs(curr+[nums[i]], s+nums[i], i+1)
        dfs([], 0, 0 )
        print(res)
        return res     