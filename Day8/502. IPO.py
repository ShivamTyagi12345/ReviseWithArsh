class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap = []
        projects = list(zip(capital, profits))
        projects.sort()
        l = len(profits)
        
        ptr = 0

        for _ in range(k):
            # this loop finds 1 project everytime till k

            # Finding Available Projects
            # Adding maximum among those
            # Continue k times
            while ptr < l and  w >= projects[ptr][0]:
                heappush(heap, -projects[ptr][1])
                ptr +=1
            if not heap:
                break
            w += -heappop(heap)
        return w
            
                    

                

            