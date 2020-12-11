"""
Author: Tanner Shimanek
Date: December 3, 2020
Description: Driver Module for graph(BETA).py
"""
from graph import Graph
import math


def main():
    """Driver function for graph(BETA).py."""
    g = Graph()

    # Add vertices
    vertices = ['A', 'B', 'C', 'D', 'E', 'F']
    # vertices = ['F', 'B', 'A', 'C', 'E', 'D']
    for vertex in vertices:
        g.add_vertex(vertex)

    # Add edges
    g.add_edge('A', 'B', 2.0)
    g.add_edge('A', 'F', 9.0)
    g.add_edge('B', 'F', 6.0)
    g.add_edge('B', 'D', 15.0)
    g.add_edge('B', 'C', 8.0)
    g.add_edge('C', 'D', 1.0)
    # g.add_edge('D', 'E', 0)
    g.add_edge('E', 'C', 7.0)
    g.add_edge('E', 'D', 3.0)
    g.add_edge('F', 'E', 3.0)

    # Testing Methods
    g.display_graph()
    # g.display()
    # print(g.get_weight('B', 'A'))
    # print(g.get_weight('B', 'C'))
    # print(g.dfs('A'))
    # print(g.bfs('A'))
    # print(g)
    # print(g.get_graph())
    print(g.dijkstra_shortest_path('A', 'C'))
    # print(g.dijkstra_shortest_path('B', 'C'))
    print(g)
    # g.get_weight('A', 'G')
    # g.display_vertices()
    # g.display_graph()
    # print(g)
    # print(test_output())
    # print(test_output_single_vertex())
    # print(type(math.inf))

# ------ TESTING FUNCTIONS ------ #



main()

# for vertex in self.graph:
#     weight = self.get_weight(src, vertex)
#     if vertex == src:
#         results[vertex] = (0.0, None)
#         visited.append(True)
#     elif vertex in self.graph[src]:
#         results[vertex] = (weight, src)
#         visited.append(False)
#     else:
#         results[vertex] = (math.inf, None)
#         visited.append(False)
