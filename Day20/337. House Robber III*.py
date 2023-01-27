# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def fun(flg,root,memo):
    if(root==None):
        return 0
    if((root,flg) in memo):
        return memo[(root,flg)]
    if(flg==1):
        a=fun(0,root.left,memo)+fun(0,root.right,memo)
        memo[(root,flg)]=a
        return a
    a=fun(0,root.left,memo)+fun(0,root.right,memo)
    b=fun(1,root.left,memo)+fun(1,root.right,memo)+root.val
    x=max(a,b)
    memo[(root,flg)]=x
    return x
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo={}
        return(fun(0,root,memo))