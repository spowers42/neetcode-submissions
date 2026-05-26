# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # simple version
        # use DFS to create a sorted array
        # take the k-1 element from array
        # uses O(n) extra memory

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            array.append(node.val)
            inorder(node.right)

        array = []
        inorder(root)
        return array[k - 1]
