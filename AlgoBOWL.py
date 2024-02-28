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

# Test if the graph is a DAG
with open('output.txt', 'w') as file:
    while not nx.is_directed_acyclic_graph(course_graph):
        num_nodes = course_graph.number_of_nodes()

        #Pagerank
        course_mat = np.zeros((num_nodes, num_nodes))

        for node, out_degree in course_graph.out_degree():
            for nodepointto in course_graph.successors(node):
                course_mat[nodepointto-1, node-1] = 1/out_degree
        
        eigenvalues, eigenvectors = np.linalg.eig(course_mat)

        # Find the index of the eigenvalue equal to 1
        index = np.where(np.isclose(eigenvalues, 1))[0]

        eigenvector = np.abs(eigenvectors[:, index[0]])
        nodetoremove = np.argmax(eigenvector) + 1
        course_graph.remove_node(nodetoremove)
        file.write(str(nodetoremove)+'\n')
