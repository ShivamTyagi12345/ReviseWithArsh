class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merged_value(a: List[int], b:List[int])-> List[int]:
            i , j = 0, 0
            res = []
            while i< len(a) and j< len(b):
                if a[i] < b[j]:
                    res.append(a[i])
                    i +=1
                else:
                    res.append(b[j])
                    j +=1
            while i< len(a):
                res.append(a[i])
                i +=1
            while j< len(b):
                res.append(b[j])
                j +=1
            # print(res)
            return res


        def mergesort(arr):
            if len(arr)==1:
                return arr
            mid = len(arr)//2
            left = mergesort(arr[0: mid])
            right = mergesort(arr[mid: len(arr)])
            return merged_value(left, right)

        return(mergesort(nums) )      
        

        