# contains the Graph class and it's functions

import csv

class Node: # defines the node class: with name(str) and adj(int, arr)
    def __init__ (self, name):
        self.name = name
        self.adj = list()
        self.seen = 0
        self.match = -1

class Graph: # contains the nodes array containing Node objects
    def __init__ (self):
        self.nodes = list()
        self.name_index = list() # To be removed after debugging
        self.row_length = 0
        self.column_length = 0
        self.u = []
        self.v = []
    # Class Functions

    def add_new(self, new_name):
        self.nodes.append(Node(new_name))
        self.name_index.append(new_name) ##
        return len(self.nodes)-1

    def add_adj(self, index, adj):
        self.nodes[index].adj.append(adj)
        self.nodes[adj].adj.append(index)
        self.name_index[index] += " -> " ##
        self.name_index[index] +=  self.nodes[adj].name ##
        self.name_index[adj] += " -> " ##
        self.name_index[adj] +=  self.nodes[index].name ##        
        return self.nodes[index].adj

    def query_name(self, index):
        return self.nodes[index].name

    def query_adj(self, index):
        return self.nodes[index].adj

    def query_index(self, node):
        return self.nodes.index(node)

    def delete_adj(self, index, adj):
        self.nodes[index].adj.remove(adj)
        self.nodes[adj].adj.remove(index)



def fetch_csv(csvfile):
    raw_graph = Graph()
    # row_lenght = 0
    data = list(csv.reader(open(csvfile)))

    for i in data[0]:
        print(i)
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


class Queue:
    def __init__(self):
        self.items = list(Node)

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def match(graph): # Redundant function that calls the divider function (functionception)
    graph = divider(graph)
    return graph


def divider(graph): # Divides the nodes into two: u and v
    for i in range(0, graph.row_length):
        if graph.nodes[i].match == -1 and not i in graph.u:
            graph.u.append(i)
    for i in range (graph.row_length, len(graph.nodes)):
        if graph.nodes[i].match == -1 and not i in graph.v:
            graph.v.append(i)
    for i in graph.u:
        graph = path_finder(graph, i, [])
    return graph


def path_finder(graph, node_index, path): # A dfs traversal which looks for augmenting paths and calls the augment function when it finds one
    path.append(node_index)
    print("Passed", str(node_index))
    if node_index in graph.u:
        print ("Node_index is in u")
        if graph.nodes[node_index].match == -1:
            print("It is not connected to anything, going to", graph.nodes[node_index].adj[0])
            graph = path_finder(graph, graph.nodes[node_index].adj[0], path)
        elif graph.nodes[node_index].match != -1:
            print("The node is connected looking for another unconnected node")
            if graph.nodes[node_index].match != graph.nodes[node_index].adj[0]:
                path_finder(graph, graph.nodes[node_index].adj[0], path)
            else:
                try: 
                    path_finder(graph, graph.nodes[node_index].adj[1], path)
                except:
                    print("hela")

    if node_index in graph.v:
        print (str(node_index), "is in v")
        if graph.nodes[node_index].match == -1:
            print("It is not matched.")
            print("Augmenting path:", path)
            graph = augment(graph, path)   
        else:
            print("This node in v is matched, going to", graph.nodes[node_index].match)
            path_finder(graph, graph.nodes[node_index].match, path)        
    return graph


def augment(graph, path): # Function that augments the path when passed an array of node indices
    print("Augmenting initiated")
    for i in range(0, len(path)-1):
        print("Dealing with", path[i], path[i+1])
        if graph.nodes[path[i]].match == path[i+1] or graph.nodes[path[i+1]].match == path[i]:
            # graph.nodes[path[i]].match = -1
            graph.nodes[path[i+1]].match = -1
            print("Unmatched", path[i], "<->", path[i+1])
        else:
            graph.nodes[path[i]].match = path[i+1]
            graph.nodes[path[i+1]].match = path[i]
            print("Matched", path[i], "->", graph.nodes[path[i]].match)
            print("Matched", path[i+1], "->", graph.nodes[path[i+1]].match)
    return graph

graph1 = fetch_csv("data.csv")

graph1 = match(graph1)

print ("\n\n\n\n\n ----------\n ONE WAY OF MAXIMAL MATCHING IS:")
for i in range(0, len(graph1.nodes)):
    if graph1.nodes[i].match != -1:
        print(graph1.nodes[i].name, "->", graph1.nodes[graph1.nodes[i].match].name)

print("\n You can also refer to output.csv for exporting the data")

csvwrite(graph1)