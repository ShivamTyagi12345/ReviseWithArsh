class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        n = 120
        s = str(n)
        # rev = int(s[::-1])
        # print(s[::-1])
        # print(rev)

        rev = list(map(lambda s : int(str(s)[::-1]), nums))

        # for item in rev:
        #     print(item)
        count = 0
        l = len(nums)
        for i in range(l):
            for j in range(i+1, l):
                if nums[i]+ rev[j]  == nums[j] + rev[i]:
                    count +=1
        return count % 10**9+7
        