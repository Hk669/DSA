from collections import defaultdict
class Solution:
    def pathExists(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        adjacency_list = defaultdict(list)
        # adjacency_list = {i: [] for i in range(n)}
        for u, v in edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)

        visited = set()

        def dfs(node):
            if node == destination:
                return True
            visited.add(node)
            for neighbour in adjacency_list[node]:
                if neighbour not in visited:
                    if dfs(neighbour):
                        return True
                
            return False
        return dfs(source)