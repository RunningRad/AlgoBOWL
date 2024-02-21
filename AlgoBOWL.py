import matplotlib.pyplot as plt
import networkx as nx
import sys

# File input for the project
input = sys.argv[1]
lines = []
with open(input, 'r') as file:
    for line in file:
        noSlashInLine = line.rstip('\n')
        lines.append(noSlashInLine)


