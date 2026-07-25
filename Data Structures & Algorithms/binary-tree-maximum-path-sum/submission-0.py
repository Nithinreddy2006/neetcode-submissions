# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        
        def max_gain(node):
            if not node:
                return 0
            
            # Only take positive gains from children; ignore negative paths
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            # Best path sum if this node is the "highest" point of the path
            price_newpath = node.val + left_gain + right_gain
            self.max_sum = max(self.max_sum, price_newpath)
            
            # Return the max gain if continuing the path through this node
            # upward to its parent (can only take one branch, not both)
            return node.val + max(left_gain, right_gain)
        
        max_gain(root)
        return self.max_sum