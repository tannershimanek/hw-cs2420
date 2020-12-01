"""
Author: Tanner Shimanek
Date: December 1, 2020
Description: A graph ADT.
"""



class Graph:
    """A python graph ADT."""

    def __init__(self):
        pass

    def add_vertex(self, label):
        """add a vertex with the specified label.
        Return the graph. label must be a string or
        raise ValueError.
        """
        print('TODO: add_vertex()')
        return -1

    def add_edge(self, src, dest, w):
        """add an edge from vertex src to vertex dest
        with weight w. Return the graph. validate src,
        dest, and w: raise ValueError if not valid.
        """
        print('TODO: add_edge()')
        return None

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
        return -1

    def dijkstra_shortest_path_D(self, src) -> dict:
        """Return a dictionary of the shortest weighted
        path between src and all other vertices using
        Dijkstra's Shortest Path algorithm. In the
        dictionary,the key is the vertex label, the value
        is a tuple(path length , the list of vertices on
        the path from key back to src).
        """
        print('TODO: dijkstra_shortest_path()')
        return -1

    def __str__(self):
        """Produce a string representation of the graph
        that can be used with print().
        """
        print('TODO print graph')