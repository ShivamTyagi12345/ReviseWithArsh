#Referred to https://leetcode.com/problems/most-profitable-path-in-a-tree/solutions/2886863/python-detailed-explanation-dfs-backtracking-codeplug/?languageTags=python3

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adjMat, n = defaultdict(list), len(amount)

        for u, v in edges:
            adjMat[u].append(v)
            adjMat[v].append(u)

        bobPath, bobPathVisited = None, set()

        def findBobPath(node, currPath): # find shortest bob path to root
            currPath.append(node)
            bobPathVisited.add(node)
            if node == 0:
                nonlocal bobPath
                if bobPath is None or len(currPath) < bobPath: bobPath = currPath[:]
                return

            for nei in adjMat[node]:
                if nei not in bobPathVisited: findBobPath(nei, currPath)
            currPath.pop()

        findBobPath(bob, [])
        res, visited, bobVisited = -inf, set(), set()

        def solveAlice(node, alice, i): # consider i as time, alice is the score accumulated, node is the current node of alice
            visited.add(node)

            if node > 0 and len(adjMat[node]) == 1:
                nonlocal res
                if node in bobVisited: pass
                elif i < len(bobPath) and bobPath[i] == node: alice += amount[node] // 2
                else: alice += amount[node]
                res = max(res, alice)
                return

            if node in bobVisited: pass # if node already visited by bob ignore the amount
            elif i < len(bobPath) and bobPath[i] == node: alice += amount[node] // 2 # if at a given time i, both alice and bob are at same node, only add half of amount to alice
            else: alice += amount[node] # if node not visited by bob by given time i, add full amount to alice

            if i < len(bobPath): bobVisited.add(bobPath[i]) # if i < len(bobPath) means bob has not yet reached the root, so add the node at time i in bobPath to bobVisited

            for nei in adjMat[node]:
                if nei not in visited: solveAlice(nei, alice, i + 1)

            if i < len(bobPath): bobVisited.discard(bobPath[i]) # backtrack bobVisited according to time i

        solveAlice(0, 0, 0)
        return res