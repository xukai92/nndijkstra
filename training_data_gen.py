from subprocess import Popen, PIPE

N = 1000
NODE_NUM = 10
EDGE_NUM = 50
WEIGHT_MAX = 100

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
    dis_max = max(data_vec[1:])

    # Only edges
    edges = " ".join(map( lambda i: str(i), data_vec[1:]))

    # Output
    f.write("{edges} {dis_max}\n".format(edges=edges, dis_max=dis_max))

f.close()