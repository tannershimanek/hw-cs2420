"""
Author: Tanner Shimanek
Date: December 1, 2020
Description: A graph ADT.
"""


class Graph:
    """A python graph ADT."""

    def __init__(self):
        """Initialize Graph and vertices."""
        self.graph = []
        self.vertices = []
        self.num_vertices = 0

    def add_vertex(self, label: str):
        """add a vertex with the specified label.
        Return the graph. label must be a string or
        raise ValueError.
        """
        # TODO: Validate label type(str)
        if label in self.vertices:
            print('Vertex ', label, "already exists.")
        else:
            self.num_vertices += 1
            self.vertices.append(label)
            if self.num_vertices > 1:
                for vertex in self.graph:
                    vertex.append(0)
            temp = []
            for _ in range(self.num_vertices):
                temp.append(0)
            self.graph.append(temp)

    def add_edge(self, src, dest, w):
        """add an edge from vertex src to vertex dest
        with weight w. Return the graph. validate src,
        dest, and w: raise ValueError if not valid.
        """
        # TODO: validate src
        # TODO: validate dest
        # TODO: validate w
        if src not in self.vertices:
            print('Vertex ', src, ' does not exist.')
        elif dest not in self.vertices:
            print('Vertex ', dest, ' does not exist')
        else:
            index1 = self.vertices.index(src)
            index2 = self.vertices.index(dest)
            self.graph[index1][index2] = w

    def get_weight(self, src, dest) -> float:
        """Return the weight on edge src-dest (math.inf
        if no path exists, raise ValueError if src or
        dest not added to graph).
        """
        print('TODO: get_weight()')
        return -1

    def dfs(self, starting_vertex):
        """Return a generator for traversing the graph
        in depth-first order starting from the specified
        vertex. Raise a ValueError if the vertex does
        not exist.
        """
        print('TODO: dfs()')
        return -1

    def bfs(self, starting_vertex):
        """Return a generator for traversing the graph
        in breadth-first order starting from the specified
        vertex. Raise a ValueError if the vertex does not 
        exist.
        """
        print('TODO: bfs()')
        return -1

    def dijkstra_shortest_path(self, src, dest) -> list:
        """ Return a tuple (path length , the list of
        vertices on the path from dest back to src). If
        no path exists, return the tuple (math.inf,
        empty list.)
        """
        print('TODO: dijkstra_shortest_path()')
        return [None]

    def dijkstra_shortest_path_D(self, src) -> dict:
        """Return a dictionary of the shortest weighted
        path between src and all other vertices using
        Dijkstra's Shortest Path algorithm. In the
        dictionary,the key is the vertex label, the value
        is a tuple(path length , the list of vertices on
        the path from key back to src).
        """
        print('TODO: dijkstra_shortest_path()')
        return {}

    def __str__(self):
        """Produce a string representation of the graph
        that can be used with print().
        """
        return 'TODO: print graph'

    # ------ TESTING METHODS ------ #

    def display(self):
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if self.graph[i][j] != 0:
                    print(self.vertices[i], " -> ", self.vertices[j],
                          " edge weight: ", self.graph[i][j])
