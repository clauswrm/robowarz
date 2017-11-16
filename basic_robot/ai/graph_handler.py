class Node():
    def __init__(self, parent):
        self.parent = parent
        self.children = []

    def add_child(self, child):
        self.children.append(child)


class Graph_Handler():
    # Denne klassen holder styr på hvor vi er i grafen, og hvilke retninger vi må kjøre/svinge for å utforske den
    # Vi starter med å anta at den kanten bilen settes ned på og startes fra har sitt opphav i rotnoden. Dermed
    # begynner vi med å lage objektet start_node. Bilen kjører så fram til det støter på et kryss eller en "node",
    # Der det bruker rutinen add_node() for å legge til den nye noden i treet. Bilen vil så velge en retning å gå derfra
    # (typ høyre/venstre) og gjentar prosessen.
    # Om teipen plutselig tar slutt vil bilen registrere dette som en løvnode, snu 180 grader, og finne veien tilbake til
    # forrige node gitt av DFS-stakken

    def __init__(self):
        # mengden med noder
        self.nodes = set()
        # rotnoden legges til treet
        start_node = Node(None)
        self.nodes.add(start_node)
        self.current_edge = [start_node, None]
        self.previousNode = start_node

    def calculate_path_to(self):
        pass
    
    def add_node(self):
        parent = self.current_edge[0]
        node = Node(parent)
        parent.add_child(node)

    def handle_crossroads(self):
        # Denne metoden bør kalles av en annen metode/objekt som har konkludert med at vi har kommet til en ny non-leaf node
        # Håndterer handlingsmønsteret når vi kommer til en non-leaf node, enten vi har sett den før eller ikke

        # Hvis vi ikke har vært i noden før må vi legge det til i det kjente nettverket
        if (self.current_edge[1] == None):
            self.add_node()
            # TODO: Legge til måter å utforske/klassifisere noden. I praksis finne ut av om den har to eller tre barn
            # Dette er et stretch goal. Blir nok ikke implementert


            # Hvis noden er
            # TODO: opprette en "path"-liste eller lignende
            # TODO: Hvis vi kommer til den noden vi er på vei til MTP DFS: Søke videre i treet
            # TODO: Hvis ikke, velge riktig retning for å komme oss til noden.
