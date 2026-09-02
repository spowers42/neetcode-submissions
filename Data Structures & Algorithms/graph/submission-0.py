class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, src: int, dst: int) -> None:
        self.graph[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        removed = False
        if src in self.graph and dst in self.graph[src]:
            self.graph[src].remove(dst)
            removed = True
        return removed

    def hasPath(self, src: int, dst: int) -> bool:
        if src not in self.graph:
            return False

        visited = set()
        q = deque()

        q.append(src)

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node == dst:
                    return True
                for next_node in self.graph[node]:
                    q.append(next_node)

        return False
