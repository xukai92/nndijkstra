#!usr/bin/env python
import sys

class Graph:
    def __init__(self, N, edgeWeight):
        self.N = N
        self.edgeWeight = edgeWeight

def dijkstra(graph, src):
    """
    Return a distanceTo[] and pathTo[] array pair.
    """
    N = graph.N
    unvisited = range(N)
    distanceTo = [float("inf") for i in range(N)]
    pathTo = [None for i in range(N)]

    distanceTo[src] = 0

    while len(unvisited) > 0:
        # select u from unvisited with min distanceTo[u]
        min_dist = float("inf")
        u = None
        for i in unvisited:
            if distanceTo[i] < min_dist:
                min_dist = distanceTo[i]
                u = i

        unvisited.remove(u)

        for v in unvisited:
            alt = distanceTo[u] + graph.edgeWeight[u][v]
            if alt < distanceTo[v]:
                distanceTo[v] = alt
                pathTo[v] = u

    return (distanceTo, pathTo)

if __name__ == "__main__":
    # Read in random graphs.
    graph_str = sys.stdin.readlines()
    graphs = [] # Hold all graphs.
    for idx, line in enumerate(graph_str):
        str_list = line.split()
        N = int(str_list[0])
        assert len(str_list) == (N * N + 1), "Line " + idx + " has incorrect number of inputs."

        edgeWeight = []
        for i in range(N):
            weightFromI = []
            for j in range(N):
                weightFromI.append(int(str_list[ 1 + (i * N) + j ]))

            edgeWeight.append(weightFromI)

        # Construct Graph object
        graphs.append(Graph(N, edgeWeight))

    for graph in graphs:
        N = graph.N
        print N
        for i in range(N):
            dist, path = dijkstra(graph, i)
            print ", ".join([str(j) for j in dist])
