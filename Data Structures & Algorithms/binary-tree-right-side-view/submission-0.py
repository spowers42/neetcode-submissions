# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        result = []

        if root:
            q.append(root)

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if i == 0:
                    result.append(node.val)
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)

        return result
