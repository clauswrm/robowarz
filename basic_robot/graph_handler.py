
class Node():
    def __init__(self,parent):

        self.parent = parent
        self.children = []

    def add_child(self,child):
        self.children.append(child)


class Graph_Handler():

    def __init__(self):
        self.nodes = set()
        start_node = Node(None)
        self.nodes.add(start_node)
        self.current_edge = [start_node,None]


    def add_node(self):
        parent = self.current_edge[0]
        node = Node(parent)
        parent.add_child(node)

    def handle_crossroads(self):
        #hva gjør vi når vi kommer til et kryss?

        #Hvis vi ikke har vært i krysset før må vi legge det til i det kjente nettverket
        if(self.current_edge[1]==None):
            self.add_node()
            #TODO: Legge til måter å utforske og evt klassifisere noden.

        #Hvis noden er
        #TODO: opprette en "path"-liste eller lignende
        #TODO: Hvis vi kommer til den noden vi er på vei til MTP DFS: Søke videre i treet
        #TODO: Hvis ikke, velge riktig retning for å komme oss til noden.



