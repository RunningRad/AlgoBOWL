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

print(number_of_edges(course_graph))