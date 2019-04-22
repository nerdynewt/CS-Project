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

u = []
v = []

def match(graph):
    divider(graph)
    graph = path_finder(graph)
    return graph

def divider(graph):
    for i in graph.nodes in range (0, graph.row_length):
        if i.match == -1:
            u.append(i.query_index)
    for i in graph.nodes in range (graph.row_length, len(graph.nodes)):
        if i.match == -1:
            v.append(i.query_index)

    print("u:", u)
    print("v:", v)

    # u = [i for i in graph.nodes.query_index in range (0, graph.row_length) & graph.nodes[i].match == -1]
    # v = [i for i in graph.nodes.qery_index in range (graph.row_length, len(graph.nodes)) & graph.nodes[i].match == -1]


def path_finder(graph):    
  
    for node_index in u:
        if graph.nodes[node_index].match == -1:
            graph = dfs(graph, u)
        else:
            u.remove(u)
    return graph

def dfs(graph, node_index):
    path = list()
    if node_index in u:
        for i in graph.nodes[node_index].adj:
            if graph.nodes[i].match == -1:
                path.append(i)
                dfs(graph, graph.nodes[i])
            else:
                u.remove(graph.query_index(i))
    if node_index in v:
        for i in graph.nodes[node_index].adj:
            if graph.nodes[i].match != -1:
                path.append(i)
                dfs(graph, graph.nodes[i])
            else:
                graph = augment(graph, path)
    return graph


def augment(graph, path):
    for i, j in zip(path, path[1:]):
        if graph.nodes[i].match != -1:
            graph.nodes[i].match = -1
        elif graph.nodes[i].match == -1:
            graph.nodes[i].match = j
        return graph

# def augment(graph, path):
#      for nodes, next in zip(path, path[1:]):
#         if nodes.match != -1:
#             nodes.match = -1
#         elif nodes.match == -1:
#             nodes.match = graph.query_index(next)
#         else:
#             print("Nigga wha?")
