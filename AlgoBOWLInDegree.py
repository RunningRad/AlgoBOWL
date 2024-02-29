import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import sys

# File input for the project
input = sys.argv[1]
lines = []
with open(input, 'r') as file:
    for line in file:
        noSlashnLine = line.rstrip('\n')
        lines.append(noSlashnLine)

#number of courses
n = int(lines[0].split()[0])


#nodes
course_graph = nx.DiGraph()
for i in range(n):
    course_graph.add_node(i+1)

#add edges and
#tracking what node were on
curr_node = 1
for node in lines[1:]:
    for i in range(int(lines[curr_node].split()[0])):
        course_graph.add_edge(int(lines[curr_node].split()[i+1]), curr_node)
    curr_node += 1

with open('output.txt', 'w') as file:
    nodes_to_del = []
    while not nx.is_directed_acyclic_graph(course_graph):
        nodeTarget = list(course_graph.nodes)[0]
        x = 0
        for n in course_graph:
            if course_graph.degree(n) > course_graph.degree(nodeTarget):
                if course_graph.in_degree(n) > 0 and course_graph.out_degree(n) > 0:
                    nodeTarget = n
            x = x + 1
        nodes_to_del.append(nodeTarget)
        course_graph.remove_node(nodeTarget)

    file.write(str(len(nodes_to_del)) + '\n')
    for node in nodes_to_del:
        file.write(str(node) + " ")


