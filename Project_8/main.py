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
    g.display()
    print(g.get_weight('A', 'B'))
    print(g.dfs('A'))
    print(g.bfs('A'))
    print(g)
    # print(g.get_graph())
    # print(g.dijkstra_shortest_path('A', 'C'))
    # # print(g)
    # g.get_weight('A', 'G')
    # g.display_vertices()
    # g.display_graph()
    # print(g)
    # print(test_output())
    # print(test_output_single_vertex())

# ------ TESTING FUNCTIONS ------ #


def test_output():
    correct_output = "numVertices: 6\n" \
                     "Vertex \t Adjacency List\n" \
                     "A \t\t [('B', 2.0), ('F' 9.0)]\n" \
                     "B \t\t [('F', 6.0), ('D', 15.0), ('C', 8.0)] \n" \
                     "C \t\t [('D', 1.0)]\n" \
                     "D \t\t []\n" \
                     "E \t\t [('C', 7.0), ('D', 3.0)]\n" \
                     "F \t\t [('E', 3.0)]\n"
    return correct_output


def test_output_single_vertex():
    correct_output = "starting BFS with vertex A\n" \
                     "A\n" \
                     "B\n" \
                     "F\n" \
                     "D\n" \
                     "C\n" \
                     "E\n"
    return correct_output


main()
