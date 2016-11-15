from subprocess import Popen, PIPE

N = 10
NODE_NUM = 8
EDGE_NUM = 16
WEIGHT_MAX = 16

f = open('training.txt', 'w')

for i in range(N):
    # Run random graph generator
    p1 = Popen(["python", "rand_graph_gen.py", str(NODE_NUM), str(EDGE_NUM), str(WEIGHT_MAX)], stdout=PIPE)
    rand_graph, _ = p1.communicate()

    # Run Dijkstra's
    p2 = Popen(["python", "dijkstra.py"], stdin=PIPE, stdout=PIPE)
    dij_output, _ = p2.communicate(input=rand_graph)

    # Turn output to a vector; fxxk Neil
    data_vec = map(lambda s: int(s), ", ".join(dij_output.split("\n")).split(", ")[:-1])

    # Find the maximum distance from the source
    print data_vec[2:NODE_NUM+2]
    dis_min = min(filter(lambda w: w > 0, data_vec[2:NODE_NUM+2]))

    # Only edges
    graph_vec = map(lambda s: int(s), ", ".join(rand_graph.split(" ")).split(", ")[:-1])
    edges = " ".join(map( lambda i: str(i), graph_vec[1:]))

    # Output
    f.write("{edges} {dis_min}\n".format(edges=edges, dis_min=dis_min))

f.close()