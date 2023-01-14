# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res = []
        def dfs(root):
            if root:
                res.append(root.val)
                dfs(root.left)
                dfs(root.right)
        dfs(root1)
        print(res)
        dfs(root2)
        print(res)
        return sorted(res)


