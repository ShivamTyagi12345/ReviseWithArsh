class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for a, b in points:
            hashmap = defaultdict(list)
            for x, y in points:
                key = (x-a)*(x-a) + (y-b)*(y-b)
                # if key != 0:
                hashmap[key].append((x, y))
            # print((a, b), hashmap)
            
            for i in hashmap.keys():
                n = len(hashmap[i])
                # if n >= 2:
                res += n*(n-1)
        return res 

