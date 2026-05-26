# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallest_node(self, root):
        current = root
        while current and current.left:
            current = current.left
        return current

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                root = root.right
            elif not root.right:
                root = root.left
            else:
                min_node = self.smallest_node(root.right)
                root.val = min_node.val
                root.right = self.deleteNode(root.right, min_node.val)

        return root
