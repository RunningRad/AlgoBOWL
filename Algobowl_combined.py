import networkx as nx
import sys

for input in range (721, 798):
    # File input for the project
    inputfile = 'inputs\input_group'+str(input)+'.txt'
    lines = []
    with open(inputfile, 'r') as file:
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
    
    #lance algorithm
    nodes_to_del_la = []
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
        nodes_to_del_la.append(max_total_degree_node)

    #soumil algorithm
    def degree_difference_method(graph):
        sorted_nodes = sorted(graph.nodes(),
                            key=lambda x: graph.out_degree(x) - graph.in_degree(x),
                            reverse=True)
        courses_to_test_out = []

        for node in sorted_nodes:
            if graph.in_degree(node) > 0:
                graph.remove_node(node)
                courses_to_test_out.append(node)
            if nx.is_directed_acyclic_graph(graph):
                break
        return courses_to_test_out
    
    nodes_to_del_sa = degree_difference_method(course_graph)

    with open('output'+str(input)+'.txt', 'w') as file:
        if len(nodes_to_del_la) < len(nodes_to_del_sa):
            file.write(str(len(nodes_to_del_la))+'\n')
            for node in nodes_to_del_la:
                file.write(str(node)+' ')
        else:
            file.write(str(len(nodes_to_del_sa))+'\n')
            for node in nodes_to_del_sa:
                file.write(str(node)+' ')