import sys
import networkx as nx


def read_input(input_file):
    with open(input_file, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    n = int(lines[0])
    graph = nx.DiGraph()
    graph.add_nodes_from(range(1, n + 1))
    for i, line in enumerate(lines[1:], 1):
        parts = list(map(int, line.split()))
        for prereq in parts[1:]:
            graph.add_edge(prereq, i)
    return graph


def write_output(output_file, courses_to_test_out):
    with open(output_file, 'w') as file:
        file.write(str(len(courses_to_test_out)) + '\n')
        file.write(' '.join(map(str, sorted(courses_to_test_out))) + '\n')


def remove_cycle_nodes(graph):
    nodes_to_remove = []
    while True:
        try:
            # Detects a cycle and removes an arbitrary node from it
            cycle = nx.find_cycle(graph, orientation='original')
            # Heuristic: Remove the node with the highest total degree in the cycle
            node_to_remove = max(cycle, key=lambda node: graph.in_degree(node[0]) + graph.out_degree(node[0]))[0]
            graph.remove_node(node_to_remove)
            nodes_to_remove.append(node_to_remove)
        except nx.exception.NetworkXNoCycle:
            # If there's no cycle, break out of the loop
            break
    return nodes_to_remove


def main(input_file, output_file):
    course_graph = read_input(input_file)
    courses_to_test_out = remove_cycle_nodes(course_graph)
    write_output(output_file, courses_to_test_out)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input_file.txt output_file.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    main(input_file, output_file)
