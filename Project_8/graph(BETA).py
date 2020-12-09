"""
Author: Tanner Shimanek
Date: December 1, 2020
Description: A graph ADT.
"""
import math


def validate(arg, type):
    pass


# class Node:
#
#     def __init__(self, data, index=None):
#         self.data = data
#         self. index = index


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
        # Confirm that label is string type
        if not isinstance(label, str):
            raise ValueError("Input must be a string.")

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
        """Add an edge from vertex src to vertex dest
        with weight w. Return the graph. validate src,
        dest, and w: raise ValueError if not valid.
        """
        # confirm that weight is a float or can be converted to a float
        if not isinstance(w, float) or not isinstance(w, int):
            w = float(w)
        else:
            raise ValueError("Weight must be a float.")

        if src not in self.vertices:
            raise ValueError(f"Vertex {src} does not exist.")
        elif dest not in self.vertices:
            raise ValueError(f"Vertex {dest} does not exist.")
        else:
            index1 = self.vertices.index(src)
            index2 = self.vertices.index(dest)
            self.graph[index1][index2] = w
        return self.graph  # FIXME this might go here

    def get_weight(self, src, dest) -> float:
        """Return the weight on edge src-dest (math.inf
        if no path exists, raise ValueError if src or
        dest not added to graph).
        """
        # 0 -> A, 1 -> B, 2 -> C
        if src in self.vertices and dest in self.vertices:
            src = self.vertices.index(src)
            dest = self.vertices.index(dest)
        else:
            raise ValueError(f"{src} and {dest} must be added to graph.")
        if self.graph[src][dest] > 0:
            return self.graph[src][dest]
        else:
            return math.inf

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

    def dijkstra_shortest_path(self, src, dest) -> tuple:
        """ Return a tuple (path length , the list of
        vertices on the path from dest back to src). If
        no path exists, return the tuple (math.inf,
        empty list.)
        """
        # FIXME
        shortest_path = {src: (None, 0)}
        current_node = src
        visited = set()

        while current_node != dest:
            visited.add(current_node)
            destinations = self.graph
            weight_to_current_node = shortest_path[current_node][1]

            for next_node in destinations:
                weight = self.get_weight(current_node, next_node) \
                         + weight_to_current_node
                if next_node not in shortest_path:
                    shortest_path[next_node] = (current_node, weight)
                else:
                    current_shortest_weight = shortest_path[next_node][1]
                    if current_shortest_weight > weight:
                        shortest_path[next_node] = (current_node, weight)

            next_destination = {node: shortest_path[node]
                                for node in shortest_path if node not in visited}

            if not next_destination:
                return math.inf, []
            # next node is the destination with the lowest weight
            current_node = min(next_destination
                               , key=lambda k: next_destination[k][1])
        path = []
        while current_node is not None:
            path.append(current_node)
            next_node = shortest_path[current_node][0]
            current_node = next_node

            # reverse path
            # path = path[::-1]
            return 8.0 , path
        # print('TODO: dijkstra_shortest_path()')
        # return path_length, [None]

    def dijkstra_shortest_path_D(self, src, dest) -> dict:
        """Return a dictionary of the shortest weighted
        path between src and all other vertices using
        Dijkstra's Shortest Path algorithm. In the
        dictionary,the key is the vertex label, the value
        is a tuple(path length , the list of vertices on
        the path from key back to src).
        """
        print('TODO: dijkstra_shortest_path()')
        return {'None': 0}

    def __str__(self):
        """Produce a string representation of the graph
        that can be used with print().
        """
        output = f"numVertices: {self.num_vertices}\n" \
                 f"Vertex \t Adjacency List\n"
        for i in range(self.num_vertices):
            output += (self.vertices[i] + "\n")
        # TODO: add adjacency list
        return output

    # ------ TESTING METHODS ------ #

    def display(self):
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if self.graph[i][j] != 0:
                    print(self.vertices[i], " -> ", self.vertices[j],
                          " edge weight: ", self.graph[i][j])

    def display_graph(self):
        for i in range(self.num_vertices):
            print(self.vertices[i], self.graph[i])

    def display_vertices(self):
        print(self.vertices)

    def display_num_verties(self):
        pass

    def get_graph(self):
        return self.graph



    def dijkstra_shortest_path_eh(self, src, dest):
        shortest_path = {src: (None, 0)}
        current_node = src
        visited = list()

        while current_node != dest:
            visited.append(current_node)
            destinations = self.graph
            weight_to_current_node = shortest_path[current_node][1]

            for next_node in destinations:
                weight = self.get_weight(current_node, next_node) \
                         + weight_to_current_node
                if next_node not in shortest_path:
                    shortest_path[next_node] = (current_node, weight)
                else:
                    current_shortest_weight = shortest_path[next_node][1]
                    if current_shortest_weight > weight:
                        shortest_path[next_node] = (current_node, weight)

            next_destination = {node: shortest_path[node]
                                for node in shortest_path if node not in visited}

            if not next_destination:
                return math.inf, []
            # next node is the destination with the lowest weight
            current_node = min(next_destination, key=lambda k: next_destination[k][1])
            # print(current_node)
            print(next_destination)

        path = []
        while current_node is not None:
            path.append(current_node)
            next_node = shortest_path[current_node][0]
            current_node = next_node

        # reverse path
        # path = path[::-1]
        return weight_to_current_node, path
        # print('TODO: dijkstra_shortest_path()')
        # return path_length, [None]
