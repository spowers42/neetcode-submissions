# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(r):
            if not r:
                return 0
            left_depth = depth(r.left)
            right_depth = depth(r.right)
            return max(left_depth, right_depth) + 1

        if not root:
            return True

        left_balanced = self.isBalanced(root.left)
        right_balanced = self.isBalanced(root.right)
        left_depth = depth(root.left)
        right_depth = depth(root.right)
        if left_balanced and right_balanced and -1 <= left_depth - right_depth <= 1:
            return True
        return False
