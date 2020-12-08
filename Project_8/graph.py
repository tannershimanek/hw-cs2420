"""
Author: Tanner Shimanek
Date: December 1, 2020
Description: A graph ADT.
"""
import math


class Graph:
    """A python graph ADT."""

    def __init__(self):
        """Initialize Graph and vertices."""
        self.graph = {}
        self.num_vertices = 0

    def add_vertex(self, label: str):
        """add a vertex with the specified label.
        Return the graph. label must be a string or
        raise ValueError.
        """
        # Confirm that label is string type
        if not isinstance(label, str):
            raise ValueError("Input must be a string.")

        if label in self.graph:
            print('Vertex ', label, ' alrady exists.')
        else:
            self.num_vertices += 1
            self.graph[label] = []

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

        if src not in self.graph:
            raise ValueError(f"Vertex {src} does not exist.")
        elif dest not in self.graph:
            raise ValueError(f"Vertex {dest} does not exist.")
        else:
            temp = [dest, w]
            self.graph[src].append(temp)
        return self.graph  # FIXME this might go here

    def get_weight(self, src, dest) -> float:
        """Return the weight on edge src-dest (math.inf
        if no path exists, raise ValueError if src or
        dest not added to graph).
        """
        # if src exists in self.graph
        if src not in self.graph:
            raise ValueError(f"{src} must be added to graph.")

        for index in self.graph[src]:
            if index[0] == dest:
                return index[1]
            else:
                # if dest does not exist in self.graph
                # raise ValueError(f"{dest} must be added to graph.")
                return math.inf

    def dfs(self, starting_vertex):
        """Return a generator for traversing the graph
        in depth-first order starting from the specified
        vertex. Raise a ValueError if the vertex does
        not exist.
        """
        visited = set()
        self._dfs_helper(visited, starting_vertex)
        # TODO: RETURN GENERATOR

    def _dfs_helper(self, visited, node):
        if node not in visited:
            print(node)  # remove later
            visited.add(node)
            for neighbor in self.graph[node]:
                self._dfs_helper(visited, neighbor[0])

    def bfs(self, starting_vertex):
        """Return a generator for traversing the graph
        in breadth-first order starting from the specified
        vertex. Raise a ValueError if the vertex does not
        exist.
        """
        visited = [starting_vertex]
        queue = [starting_vertex]
        while queue:
            s = queue.pop(0)
            print(s)  # remove later
            for neighbor in self.graph[s]:
                if neighbor[0] not in visited:
                    visited.append(neighbor[0])
                    queue.append(neighbor[0])
        # TODO: RETURN GENERATOR

    def dijkstra_shortest_path(self, src, dest) -> tuple:
        """ Return a tuple (path length , the list of
        vertices on the path from dest back to src). If
        no path exists, return the tuple (math.inf,
        empty list.)
        """
        # FIXME: idk make this work
        # shortest_path = {src: (None, 0)}
        # current_node = src
        # visited = set()

        # while current_node != dest:
        #     visited.add(current_node)
        #     destinations = self.vertices
        #     weight_to_current_node = shortest_path[current_node][1]

        #     for next_node in destinations:
        #         weight = self.get_weight(current_node, next_node) \
        #                  + weight_to_current_node
        #         if next_node not in shortest_path:
        #             shortest_path[next_node] = (current_node, weight)
        #         else:
        #             current_shortest_weight = shortest_path[next_node][1]
        #             if current_shortest_weight > weight:
        #                 shortest_path[next_node] = (current_node, weight)

        #     next_destination = {node: shortest_path[node]
        #                         for node in shortest_path if node not in visited}

        #     if not next_destination:
        #         return "Route not possible."
        #     # next node is the destination with the lowest weight
        #     current_node = min(next_destination
        #                        , key=lambda k: next_destination[k][1])
        #     path = []
        #     while current_node is not None:
        #         path.append(current_node)
        #         next_node = shortest_path[current_node][0]
        #         current_node = next_node

            # reverse path
            # path = path[::-1]
            # return 8.0, path
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
        for key, value in self.graph.items():
            output += (f'{key}' + '\t ' + f'{value}' + '\n')
        return output

    # ------ TESTING METHODS ------ #

    def display(self):
        for vertex in self.graph:
            for edges in self.graph[vertex]:
                print(vertex, " -> ", edges[0], ' edge weight: ', edges[1])

    def display_graph(self):
        print(self.graph)
