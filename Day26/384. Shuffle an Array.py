class Solution:

    def __init__(self, nums: List[int]):
        self.arr = nums
   

    def reset(self) -> List[int]:
        return self.arr

    # def permute(self, ind, arr, val)-> List[List[int]]:
    #     if ind == len(arr):
    #         temp = arr
    #         val.append(temp)
    #         print(temp)
    #         return


    #     for i in range (ind, len(arr)):
    #         arr[i], arr[ind]= arr[ind], arr[i]
    #         permute(self, ind+1, arr, val)
    #         arr[i], arr[ind]= arr[ind], arr[i]


    def shuffle(self) -> List[int]:
        ans = self.arr[:]
        for i in range(0, len(ans)):
            idx = randint(0, len(ans)-1)
            ans[i], ans[idx] = ans[idx], ans[i]
        return ans

        
        
        
    
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()