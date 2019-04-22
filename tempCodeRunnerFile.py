
    for i in range(1, len(data)):
        for j in range(1, len(data[0])):
            if data[i][j] == "1":
                raw_graph.add_adj(j, i+row_lenght)