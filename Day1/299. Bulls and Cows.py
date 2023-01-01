class Solution:
    def getHint(self, first: str, second: str) -> str:
        f_map, s_map =  defaultdict(int), defaultdict(int)
        BULL, COW = 0, 0
        for u, v in zip(first, second):
            if u == v:
                BULL +=1
            else:
                f_map[u] +=1
                s_map[v] +=1
        COW = sum(min(f_map[k], s_map[k]) for k in f_map)
        return f'{BULL}A{COW}B'