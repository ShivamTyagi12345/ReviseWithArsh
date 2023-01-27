import heapq
class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        S = {cell for row in grid for cell in row}
        heap = list(S)
        heapq.heapify(heap)
        while len(heap) > 3:
            heapq.heappop(heap)
        for i in range(m):
            for j in range(n):
                for k in range(1, min(m, n)):
                    if i - k < 0 or i + k >= m or j - k < 0 or j + k >= n:
                        break
                    curr = 0
                    for l in range(k + 1):
                        curr += grid[i+l][j+k-l] + grid[i-l][j+k-l] + grid[i+l][j-k+l] + grid[i-l][j-k+l]
                    curr -= grid[i+k][j] + grid[i-k][j] + grid[i][j+k] + grid[i][j-k]
                    if curr not in S:
                        S.add(curr)
                        heapq.heappush(heap, curr)
                        if len(heap) > 3: heapq.heappop(heap)
        return sorted(heap, reverse=True)