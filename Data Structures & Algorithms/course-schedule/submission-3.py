class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        visited = set()

        def dfs(node: Optional[int], path: set) -> bool:
            # returns True if there is a cycle
            if node in path:
                return True

            path.add(node)
            for new_node in graph[node]:
                if new_node in visited:
                    # we already did dfs on this path
                    continue
                result = dfs(new_node, path)
                if result:
                    return True
            path.remove(node)
            visited.add(node)
            return False

        for n in range(numCourses):
            result = dfs(n, set())
            if result:
                return False
        return True
