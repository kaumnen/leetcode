# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        sortarr = []
        result = 0
        
        def sortTree(root): 
            if root: 
                 
                sortTree(root.left) 
                sortarr.append(root.val) 
                sortTree(root.right)
                
            return sortarr
        
        for i in sortTree(root):
            
            if i >= L and i <= R:
                result += i
                
        return result
