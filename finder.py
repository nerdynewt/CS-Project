# Contains the most important code that does the matching
from graph import Graph
from graph import Node


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
    print("Passed", str(node_index), "to DFS function")
    if node_index in graph.u:
        print ("Node is in u")
        if graph.nodes[node_index].match == -1:
            print("It is not connected to anything, going to", graph.nodes[node_index].adj[0])
            graph = path_finder(graph, graph.nodes[node_index].adj[0], path)
        elif graph.nodes[node_index].match != -1:
            print("The node is already connected. Looking for another unconnected node in v")
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

