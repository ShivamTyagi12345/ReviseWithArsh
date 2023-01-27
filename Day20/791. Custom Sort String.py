class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dic={}
        for i in s:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        
        res=''
        for x in order:
            if x in s:
                res+=x*dic[x]
                
        for y in s:
            if y not in res:
                res+=y*dic[y]
        return res