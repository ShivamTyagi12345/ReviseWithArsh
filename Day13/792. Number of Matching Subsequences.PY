class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        res = 0
        count = 0
        
        
        
        for word in words:
            flag = 1
            pos = 0
            for c in word:
                index = s.find(c,pos)
                # print(word, c, index)
                if index ==-1:
                    flag  = 0
                    break
                pos = index+1
                
            if flag:
                count += 1
            
            
        return count