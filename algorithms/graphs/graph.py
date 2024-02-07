from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = defaultdict(list)

    def add_edge(self,u,v):
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)

    def neighbours(self, vertex):
        return self.adjacency_list[vertex]
