# Main 

from csvreader import fetch_csv
from graph import Graph
from finder import match
from csvwriter import csvwrite
# from matching import match
print("NOTE: Numbers shown are indices of nodes\n\n Progress:")

graph1 = fetch_csv("data.csv")

graph1 = match(graph1)

print ("\n\n\n\n\n ----------\n ONE WAY OF MAXIMAL MATCHING IS:")
for i in range(0, len(graph1.nodes)):
    if graph1.nodes[i].match != -1:
        print(graph1.nodes[i].name, "->", graph1.nodes[graph1.nodes[i].match].name)

print("\n You can also refer to output.csv for exporting this data")

csvwrite(graph1)
