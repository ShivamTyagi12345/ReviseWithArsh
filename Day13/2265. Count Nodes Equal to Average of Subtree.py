# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        

        def helper(root):
            nonlocal ans
            if not root:
                return (0, 0)
            

            ls, lc = helper(root.left)
           
                  
            rs, rc = helper(root.right)

            s = root.val + ls + rs

            k = 1 + lc + rc
            
            if root.val == s//k :
                ans += 1  
                # print("did something")
            # print (root.val + L[0]+ R[0], 1+L[1]+R[1])
            return (s, k)
        ans = 0
        helper(root)
        return  ans

         