# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string."""
        vals = []

        def preorder(node):
            if node is None:
                vals.append('#')
                return
            vals.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ','.join(vals)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""
        vals = iter(data.split(','))

        def build():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            return node

        return build()
