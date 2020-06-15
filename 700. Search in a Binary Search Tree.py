# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        currentNode = root
        
        while currentNode:
            if currentNode.val == val:
                return currentNode
            elif currentNode.val > val:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
                
        return None
