# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = k
        answer = -1

        def inorder(node):
            nonlocal counter, answer  # allow outerscope access
            if not node:
                return

            inorder(node.left)
            if counter == 0:
                return
            counter -= 1
            if counter == 0:
                answer = node.val
                return
            inorder(node.right)

        inorder(root)
        return answer
