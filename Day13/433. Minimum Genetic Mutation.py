class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue = [(startGene, 0)]
        seen  = [startGene]
        while queue:
            node, steps = queue.pop(0)
            if node == endGene:
                return steps
            for c in 'ATGC':
                for i in range(8):
                    neighbour = node[:i] + c + node[i+1:]
                    if neighbour not in seen and neighbour in bank:
                        queue.append((neighbour,steps+1))
                        seen.append(neighbour)
        return -1