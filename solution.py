import networkx as nx
#import matplotlib.pyplot as plt
#from pyvis.network import Network

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

def populateBoard(layout,G):
    layout=layout.split(" ")
    for x in range(len(layout)):
        G.nodes[x+1]["pos"]=int(layout[x])

#Any given tile is movable iff one of its adjacent tiles is the node with 
# the "pos" attribute set to 0. 

def isTileMovable(G,tile):
    zeroTile = (list(filter(lambda x :x[0] if x[1]['pos'] == 0 else False, G.nodes(data=True))))[0][0]
    neighbour=[x for x in G.neighbors(zeroTile)]
    if tile in neighbour:
        return True
    else:
        return False

G = makeBoard()

layout = str(input("Enter the puzzle layout in a single line, space delimited, LTR, 0 for empty tile : "))

populateBoard(layout,G)
print(isTileMovable(G,2))


#nt = Network(directed=False)
#nt.from_nx(G)
#nt.show("Puzzleboard.html",notebook=False)

#nx.draw(G,with_labels=True)
#plt.show()