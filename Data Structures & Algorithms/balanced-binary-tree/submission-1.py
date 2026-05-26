# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth_and_balanced(r):
            if not r:
                return 0, True
            left_depth, left_balanced = depth_and_balanced(r.left)
            right_depth, right_balanced = depth_and_balanced(r.right)
            is_balanced = left_balanced and right_balanced and -1 <= left_depth - right_depth <= 1
            return max(left_depth, right_depth) + 1, is_balanced

        if not root:
            return True

        _, answer = depth_and_balanced(root)
        return answer
