class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        copy = []
        res = []

        def helper(k, nums):
            nums_sorted = sorted(nums)
            kth_smallest = nums_sorted[k-1]
            index = nums.index(kth_smallest)
            return index
            # q = []
            # heapify(q)
            # hashmap = {}
            # for idx in range(len(arr)):
            #     hashmap[arr[idx]] = idx
                
            # for i in arr:
            #     heappush(q, -i)
            #     if len(q) > k:
            #         heappop(q)    
            # print("hashmap, queue, k=",hashmap, q, k)
            # return hashmap[-q[0]]

        for k, t in queries:
            # making a new array
            # print("initially copy", copy)
            copy.clear()
            for i in nums:
                copy.append(i)
            # print("restored copy ", copy)

            # assigning its value as a trimed value [str -> int]
            for idx, item in enumerate(copy):
                l = len(item)
                copy[idx] = int(item[l-t:] )
            # print("trimmed to with t=", copy, t)
            # finding the kth smallest number
            res.append(helper(k, copy))
        return res
            



                

            
            