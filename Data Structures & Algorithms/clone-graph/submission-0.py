"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None
        q = deque()

        first_node = None
        node_dict = {}

        visited = set()
        q.append(node)

        while q:
            for _ in range(len(q)):
                current = q.popleft()
                if current.val in visited:
                    continue
                if current.val in node_dict:
                    working = node_dict[current.val]
                else:
                    working = Node(current.val)
                    node_dict[current.val] = working
                    if first_node is None:
                        first_node = working
                visited.add(current.val)
                for neighbor in current.neighbors:
                    if neighbor.val not in node_dict:
                        new_node = Node(neighbor.val)
                        node_dict[neighbor.val] = new_node
                    working.neighbors.append(node_dict[neighbor.val])
                    q.append(neighbor)

        return first_node
