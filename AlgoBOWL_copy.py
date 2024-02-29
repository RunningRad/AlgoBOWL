import networkx as nx
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
    nodes_to_del = []
    while not nx.is_directed_acyclic_graph(course_graph):
        total_degrees = {node: course_graph.in_degree(node) + course_graph.out_degree(node) for node in course_graph.nodes()}
        valid_node_to_delete = False
        while not valid_node_to_delete:
            max_total_degree_node = max(total_degrees, key=total_degrees.get)

            if course_graph.in_degree(max_total_degree_node) == 0 or course_graph.out_degree(max_total_degree_node) == 0:
                del total_degrees[max_total_degree_node]
            else:
                valid_node_to_delete = True
        course_graph.remove_node(max_total_degree_node)
        nodes_to_del.append(max_total_degree_node)
    
    file.write(str(len(nodes_to_del))+'\n')
    for node in nodes_to_del:
        file.write(str(node)+' ')

        
