class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        node_to_idx = {node: idx for idx, node in enumerate(inorder)}
        self.pre_idx = 0

        def construct(left_bound: int, right_bound: int):
            if left_bound > right_bound:
                return None

            root_val = preorder[self.pre_idx]
            root_idx = node_to_idx[root_val]

            self.pre_idx += 1
            node = TreeNode(root_val)
            node.left = construct(left_bound, root_idx - 1)
            node.right = construct(root_idx + 1, right_bound)
            return node

        root = construct(0, len(inorder) - 1)
        return root
