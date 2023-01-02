class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        l = len(nums)
        LIS =[1] * l
        hashmap = defaultdict(list)
        res = []
        for i in range(l-1, -1, -1):
            largest = []
            for j in range(i+1, l):
                if nums[j] % nums[i] == 0:
                    if len(largest) < len(hashmap[j]):
                        largest = hashmap[j]
            hashmap[i].append(nums[i])
            hashmap[i].extend(largest)
            if len(res) < len(hashmap[i]):
                res = hashmap[i]
        return res
        
               


            

            
                







        