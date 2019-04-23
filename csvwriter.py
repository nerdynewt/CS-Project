# Writes the output onto a csv file

import csv
from graph import Graph, Node

def csvwrite(graph):
    clear_file = open("output.csv", 'w')
    clear_file.write("")
    clear_file.close
    output_file = open('output.csv', 'a')
    for i in range(graph.row_length, len(graph.nodes)):
        output_file.write(graph.nodes[i].name)
        output_file.write(",")
        output_file.write(graph.nodes[graph.nodes[i].match].name)
        output_file.write("\n")
    output_file.close()