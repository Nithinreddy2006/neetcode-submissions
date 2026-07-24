# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Map each value to its index in inorder for O(1) lookups
        idx_map = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0

        def build(left, right):
            # No elements to construct the subtree
            if left > right:
                return None

            # The next value in preorder is the root of this subtree
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)

            # Find the root's position in inorder to split left/right subtrees
            mid = idx_map[root_val]

            # Build left subtree first (preorder is root -> left -> right)
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)