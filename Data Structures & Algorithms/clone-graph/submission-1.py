"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if node is None:
            return None

        q = deque()
        node_to_new = {}

        new_node = Node(node.val)
        node_to_new[node] = new_node
        q.append(node)

        while q:
            for _ in range(len(q)):
                current = q.popleft()
                current_new = node_to_new[current]

                for neighbor in current.neighbors:
                    if neighbor not in node_to_new:
                        new_node = Node(neighbor.val)
                        node_to_new[neighbor] = new_node
                        q.append(neighbor)
                    new_node = node_to_new[neighbor]
                    current_new.neighbors.append(new_node)

        return node_to_new[node]
