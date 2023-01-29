class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        res = []
        vis = set()

        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
            
        print(graph)

        def dfs(path, node):
            vis.add(node)
            path.append(node)
            if node == dst:
                temp = path[:]
                # print(path)
                res.append(temp)
                # return RETURN SE ;LAUDE LAGG JATE ALL PATHS ME
            for neighbour,_ in graph[node]:
                if neighbour not in vis:
                    dfs(path, neighbour)
            path.remove(node)
            vis.remove(node)
        dfs([], src)
        
        res = filter(lambda x: len(x)==k+2, res)


        # print(list(res))
        price = float('inf')
        

        for item in list(res):
            cost = 0
            for i in range(0, len(item)-1):
                u, v = item[i], item[i+1]
                for node, weight in graph[u]:
                    if node == v:
                        # print(u, v, weight)
                        cost += weight
                        break
                # print("cost",cost)
            price = min(price, cost)
            

            
        return -1 if price == float('inf') else price


            
        
        