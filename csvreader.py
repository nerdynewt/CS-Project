# Pulls data from a csv file

import csv
from graph import Graph


def fetch_csv(csvfile):

    raw_graph = Graph()
    # row_lenght = 0
    data = list(csv.reader(open("C:\\Users\\HP\\Desktop\\CS Project\\CS-Project\\" + csvfile)))

    for i in data[0]:
        row_length = raw_graph.add_new(i) + 1

    raw_graph.row_lenght = row_length

    for i in data:
        raw_graph.add_new(i[0])

    
    for i in range(1, len(data)):
        for j in range(1, len(data[0])):
            if data[i][j] == "1":
                # print(data[0][j], "->", data[i][0])
                raw_graph.add_adj(j, i+row_length)

    return raw_graph




