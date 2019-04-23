# Pulls data from a csv file

import csv
from graph import Graph


def fetch_csv(csvfile):
    raw_graph = Graph()
    # row_lenght = 0
    data = list(csv.reader(open(csvfile)))

    for i in data[0]:
        if i != "Hello":
            raw_graph.row_length = raw_graph.add_new(i) + 1



    for i in data:
        if i[0] != "Hello":
            raw_graph.column_length = raw_graph.add_new(i[0]) +1
    
    for i in range(1, len(data)):
        for j in range(1, len(data[0])):   
            if data[i][j] == "1":
                # print(data[0][j], "->", data[i][0])
                raw_graph.add_adj(j-1, (i+raw_graph.row_length)-1)

    return raw_graph
