class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left, right, res, l = 0, 0, 0, len(s)
        hashmap = {'a': 0, 'b':0, 'c':0}
        while right < l:
            hashmap[s[right]] +=1
            while left < right  and hashmap['a'] > 0 and hashmap['b'] > 0 and hashmap['c'] > 0:
                # print(s[left: right+1])
                res += 1
                hashmap[s[left]] -=1
                left +=1
                res += len(s[right+1:]) 
            right +=1
        return res
        
        