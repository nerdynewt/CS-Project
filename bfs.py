from graph import *

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


def match(graph, node):
    invert(graph, find_path(graph, node))


def find_path(graph, node):
    u = [i for i in graph.nodes in range (0, graph.row_length)]
    v = [i for i in graph.nodes in range (graph.row_length, len(graph.nodes))]

    for nodes in u:
        if u.match == -1:
            path.append(u)
            current = graph.nodes(u.adj[0])

    return path

def dfs(graph, node):
    path = list()
    queue = Queue()
    queue.enqueue(node)
    node.seen = 1
    path.append(node)
    while not queue.isEmpty:
        node = queue.dequeue
        for i in node.adj:
            if graph.nodes[i].seen == 0 & node.match == i:
                queue.enqueue(i)
                i.seen = 1
            else:
                

def invert(graph, path):
    for nodes, next in zip(path, path[1:]):
        if nodes.match != -1:
            nodes.match = -1
        elif nodes.match == -1:
            nodes.match = graph.query_index(next)
        else:
            print("Nigga wha?")

