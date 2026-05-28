# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def _has_sum(root, current, target):
            current += root.val
            if not root.left and not root.right:
                # we are a leaf node
                return current == target

            if root.left:
                left_result = _has_sum(root.left, current, target)
                if left_result:
                    return True
            if root.right:
                right_result = _has_sum(root.right, current, target)
                if right_result:
                    return True
            return False

        if not root:
            return False
        return _has_sum(root, 0, targetSum)
