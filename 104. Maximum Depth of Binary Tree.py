# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root:
            return max(1 + self.maxDepth(root.right), 1 + self.maxDepth(root.left))
        else:
            return 0