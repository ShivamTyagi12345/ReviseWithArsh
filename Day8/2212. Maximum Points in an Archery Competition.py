class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        val = [i for i in range(12)]
        wt = [i+1 for i in aliceArrows]
        print(wt)
        res = [0]*12
        bob = []

        # n: index of the value that will be added in the iteration
        # W: the number of arrays with both
        # wt: aliceArrows array
        # val: the value of point scored
        
        def knapsack(W, n, val, wt):
            if n == 0 or W == 0:
                return 0
            #choice diagram
            # weight exhausted
            if wt[n-1] >  W:
                return knapsack(W, n-1, val, wt)
            # weight adjustable
            else:
                
                exclude = knapsack(W, n-1, val, wt)
                res[n-1] = aliceArrows[n-1] +1 
                include = val[n-1] + knapsack(W-wt[n-1], n-1, val, wt)
                res[n-1] = 0               
                return max(include, exclude)

        print(knapsack(numArrows, 12, val, wt))
        return res
        
            

                

            

            
            

            
            
            
            

            

