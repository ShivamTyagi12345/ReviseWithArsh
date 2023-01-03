class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for u, v in prerequisites:
            graph[v].append(u)
        vis = set()
        dfsvis = set()
        def dfs(child, parent):
            vis.add(child)
            dfsvis.add(child)
            for neighbour in graph[child]:

                if neighbour not in vis and dfs(neighbour, child):
                    return True
                elif neighbour in dfsvis:
                    return True
            dfsvis.remove(child)
            return False
        
        for i in range(numCourses):
            if i not in vis:
                if dfs(i, -1):
                    return False
        return True
        
                



            
