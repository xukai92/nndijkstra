#!/usr/bin/python

import sys
import random

# Helper functions for arguments and initialization
def edge_num_max(node_num):
    edge_num_sum = 0
    for node_idx in range(node_num):
        edge_num_sum = edge_num_sum + node_idx
    return edge_num_sum

def print_help():
    print "Usage: python reand_graph_gen.py node_num edge_num [max_weight] > [o_file]"
    print "NOTE: default maximum weight is 10 if not specifed"

# Get arguments
try:
    NODE_NUM = int(sys.argv[1])
    EDGE_NUM_MAX = min(int(sys.argv[2]), edge_num_max(NODE_NUM))
    if len(sys.argv) > 3:
        MAX_WEIGHT = int(sys.argv[3])
    else:
        MAX_WEIGHT = 10
except:
    print "Invalid arguments."
    print ""
    print_help()
    print ""
    print "Error Message:"
    raise

# Initialization
_unvisited, _visited = set(range(NODE_NUM)), set()
_graph = [[0 for _ in range(NODE_NUM)] for _ in range(NODE_NUM)]

# Helper functions for graph
def connect(n1, n2):
    weight = random.randint(1, MAX_WEIGHT)
    _graph[n1][n2] = weight
    _graph[n2][n1] = weight

def is_connect(n1, n2):
    return _graph[n1][n2] != 0

def visit(node):
    _unvisited.remove(node)
    _visited.add(node)

# 1. Span the graph
# Start by visiting the source node 0
# This is believed to be trival as we can always re-arrange the nodes
# to make the picked one be 0.
currnode = 0
visit(currnode)

while _unvisited:
    nextnode = random.randint(0, NODE_NUM - 1)
    if nextnode not in _visited:
        visit(nextnode)
        connect(currnode, nextnode)
        currnode = nextnode

# 2. Add randome edges till reaching EDGE_NUM_MAX
edge_num = NODE_NUM - 1

while edge_num < EDGE_NUM_MAX:
    # Pick a not fully connected node if the current is fully connected
    if len(filter(lambda w: w == 0, _graph[currnode])) == 1:
        non_full_nodes = [idx for (idx, ws) in filter(lambda (idx, ws): len(filter(lambda w: w == 0, ws)) > 1, enumerate(_graph))]
        currnode = random.sample(non_full_nodes, 1).pop()
    
    # Pick next node
    candidates = [idx for (idx, w) in filter(lambda (idx, w): idx != currnode and w == 0, enumerate(_graph[currnode]))]
    nextnode = random.sample(candidates, 1).pop()

    # Add edge
    if not is_connect(nextnode, currnode):
        connect(currnode, nextnode)
        currnode = nextnode
        edge_num = edge_num + 1

# Write to stdout
sys.stdout.write(str(NODE_NUM) + " ")
for row in range(NODE_NUM):
    for col in range(NODE_NUM):
        sys.stdout.write(str(_graph[row][col]) + " ")
sys.stdout.write("\n")
