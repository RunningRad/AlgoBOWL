import networkx as nx
import sys

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

#get output
output = sys.argv[2]

olines = []
with open(output, 'r') as file:
    for line in file:
        noSlashnLine = line.rstrip('\n')
        olines.append(noSlashnLine)

num_of_nodes_to_remove = int(olines[0])
nodes_to_remove = olines[1].split()
print(num_of_nodes_to_remove)
for i in range(0, num_of_nodes_to_remove):
    course_graph.remove_node(int(nodes_to_remove[i]))

is_good_output = nx.is_directed_acyclic_graph(course_graph)
print(is_good_output)

if (is_good_output is False):
    print(nx.find_cycle(course_graph))