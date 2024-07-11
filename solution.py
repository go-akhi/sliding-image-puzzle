import networkx as nx
#import matplotlib.pyplot as plt
from pyvis.network import Network

#the pos attribute ranges from 1 to 9 and will be the corresponding 
#node for the puzzle piece

#make the puzzleboard base
def makeBoard():
    Gr=nx.grid_2d_graph(3,3)
    mapping={}
    for x,y in Gr.nodes:
        mapping[(x,y)]=((3*int(x))+int(y)+1)
        Gr=nx.relabel_nodes(Gr,mapping)
    return Gr

G = makeBoard()

layout = str(input("Enter the puzzle layout in a single line, space delimited, LTR, 0 for empty tile : "))

def populateBoard(layout,G):
    layout=layout.split(" ")
    for x in range(len(layout)):
        G.nodes[x+1]["title"]=layout[x]

populateBoard(layout,G)

nt = Network(directed=False)
print(G.nodes(data=True))
nt.from_nx(G)
nt.show("Puzzleboard.html",notebook=False)
#nx.draw(G,with_labels=True)
#plt.show()