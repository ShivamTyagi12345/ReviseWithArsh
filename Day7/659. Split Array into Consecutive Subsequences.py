    def isPossible(self, nums: List[int]) -> bool:
        freq = dict(collections.Counter(nums))
        need = {}
        for num in nums:
            if freq[num] == 0:
                continue
            else:
                if num in need.keys() and need[num]>0:
                    freq[num] -= 1
                    need[num] -= 1
                    need[num+1] = need.get(num+1,0)+1
                elif num+1 in freq.keys() and num+2 in freq.keys() and freq[num]>0 and freq[num+1]>0 and freq[num+2]>0:
                    freq[num] -= 1
                    freq[num+1] -= 1
                    freq[num+2] -= 1
                    need[num+3] = need.get(num+3,0)+1
                else:
                    return False
        return True
