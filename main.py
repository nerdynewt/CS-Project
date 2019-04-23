# Main 

from csvreader import fetch_csv
from graph import Graph
from finder import match
# from matching import match

graph1 = fetch_csv("data.csv")
matched_graph = graph1


# for i in graph1.nodes:
#     print(i.adj)

# def match(input_graph):
#     cycle(c_graph.nodes[0])
#     matched_graph = Graph
#     return matched_graph



# def cycle(node): # Takes a node object as a parameter
#     if len(node.adj) > 1 & node.seen == 0:
#         cycle(node[node.adj[0]])
#         node.seen = 1
#     elif len(node.adj) == 1:
#         print("hello")


for i in match(graph1).nodes:
    print(i.match)

# print("Node list:", graph1.name_index)
