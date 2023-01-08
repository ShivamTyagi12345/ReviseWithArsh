class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        l = len (cards)
        res = float('inf')
        maps = defaultdict(int)
        for i in range(len(cards)):
            if cards[i] in maps:
                res = min(res, i-maps[cards[i]]+1)
            maps[cards[i]] = i        
        if res == float('inf'):
            return -1
        return res