class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts={}
        for word in words:
            counts[word]=counts.get(word,0)+1
        s_dict = {val[0] : val[1] for val in sorted(counts.items(), key = lambda x: (-x[1], x[0]))}
        print(s_dict)
        lst=[]
        x=0
        for i,j in s_dict.items():
            if(x<k):
                lst.append(i)
                x+=1
        return lst