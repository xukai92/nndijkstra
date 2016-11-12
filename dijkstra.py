#!usr/bin/env python
import sys

class Graph:
    def __init__(self, N, edgeWeight):
        self.N = N
        self.edgeWeight = edgeWeight

if __name__ == "__main__":
    # Read in random graphs.
    graph_str = sys.stdin.readlines()
    graphs = [] # Hold all graphs.
    for idx, line in enumerate(graph_str):
        str_list = line.split()
        N = int(str_list[0])
        assert len(str_list) == (N * N + 1), "Line " + idx + " has incorrect number of inputs."

        # Construct Graph object

    # For each graph, choose the single source node.
    # Call dijkstra algorithm on the graph, get back distanceTo[] and pathTo[].
