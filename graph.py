# contains the Graph class and it's functions

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