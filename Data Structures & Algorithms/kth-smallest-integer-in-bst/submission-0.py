# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        node = root
        
        while stack or node:
            # go as far left as possible
            while node:
                stack.append(node)
                node = node.left
            
            # visit the node
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            
            # move to the right subtree
            node = node.right
        
        return -1  # in case k is invalid (shouldn't happen per constraints)