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


def match(graph):
    graph = divider(graph)
    # graph = dfs(graph, 0, [])
    return graph


def divider(graph):
    for i in range(0, graph.row_length):
        if graph.nodes[i].match == -1 and not i in graph.u:
            graph.u.append(i)
    for i in range (graph.row_length, len(graph.nodes)):
        if graph.nodes[i].match == -1 and not i in graph.v:
            graph.v.append(i)
    for i in graph.u:
        graph = dfs(graph, i, [])
    return graph


def dfs(graph, node_index, path):
    path.append(node_index)
    print("Passed", str(node_index))
    if node_index in graph.u:
        print ("Node_index is in u")
        if graph.nodes[node_index].match == -1:
            print("It is not connected to anything, going to", graph.nodes[node_index].adj[0])
            graph = dfs(graph, graph.nodes[node_index].adj[0], path)
        elif graph.nodes[node_index].match != -1:
            print("The node is connected looking for another unconnected node")
            if graph.nodes[node_index].match != graph.nodes[node_index].adj[0]:
                dfs(graph, graph.nodes[node_index].adj[0], path)
            else:
                try: 
                    dfs(graph, graph.nodes[node_index].adj[1], path)
                except:
                    print("hela")

    # if node_index in graph.u:
    #     print("Node_index is in u")
    #     for i in graph.nodes[node_index].adj:
    #         print(i)
    #         if graph.nodes[node_index].match == -1:
    #             print("node is not matched")
    #             graph = dfs(graph, i, path) 
    if node_index in graph.v:
        print (str(node_index), "is in v")
        if graph.nodes[node_index].match == -1:
            print("It is not matched.")
            print("Augmenting path:", path)
            graph = augment(graph, path)   
        else:
            print("This node in v is matched, going to", graph.nodes[node_index].match)
            dfs(graph, graph.nodes[node_index].match, path)        
        # matched = -1
        # for i in graph.nodes[node_index].adj:
        #     if graph.nodes[node_index].match == i:
        #         matched = i
        # if matched == -1:
        #     print("It is not matched.")
        #     print("Augmenting path:", path)
        #     graph = augment(graph, path)
        # else:
        #     graph = dfs(graph, matched, path)
    return graph


def augment(graph, path):
    print("Augmenting initiated")
    for i, j in zip(path, path[1:]):
        print("Dealing with", i, j)
        if graph.nodes[i].match == j or graph.nodes[j].match == i:
            graph.nodes[i].match = -1
            graph.nodes[j].match = -1
            print("Unmatched", i, "<->", j)
        else:
            graph.nodes[i].match = j
            graph.nodes[j].match = i
        print("Matched", i, "->", graph.nodes[i].match)
        print("Matched", j, "->", graph.nodes[j].match)
        return graph



# def path_finder(graph):
  
#     for node_index in graph.u:
#         if graph.nodes[node_index].match == -1:
#             graph = dfs(graph, node_index)
#         else:
#             graph.u.remove(node_index)
#     return graph
