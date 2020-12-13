"""
Author: Tanner Shimanek
Date: December 3, 2020
Description: Driver Module for graph.py
"""
from graph import Graph


def main():
    """Driver function for graph(BETA).py."""
    g = Graph()
    # Add vertices
    vertices = ['A', 'B', 'C', 'D', 'E', 'F']
    for vertex in vertices:
        g.add_vertex(vertex)
    # Add edges
    g.add_edge('A', 'B', 2.0)
    g.add_edge('A', 'F', 9.0)
    g.add_edge('B', 'F', 6.0)
    g.add_edge('B', 'D', 15.0)
    g.add_edge('B', 'C', 8.0)
    g.add_edge('C', 'D', 1.0)
    g.add_edge('E', 'C', 7.0)
    g.add_edge('E', 'D', 3.0)
    g.add_edge('F', 'E', 3.0)

    # -- Testing Methods -- #
    # print(g.get_weight('A', 'B'))
    # print(g.dfs('A'))
    # print(g.bfs('A'))
    # print(g.dijkstra_shortest_path('A', 'C'))
    # print(g.dijkstra_shortest_path_All('A'))

    # -- Output -- #
    print(g)


main()
