import csv


class Graph:
    # Creates a dictionary of addresses and edges between addresses
    # STC: O(1)
    def __init__(self):
        self.delivery_list = {}
        self.edge_weights = {}

    # Adds an address vertex to the delivery list
    # STC: O(1)
    def add_vertex(self, address_vertex):
        self.delivery_list[address_vertex] = []

    # Add a new dge between to addresses
    # STC: O(1)
    def add_new_edge(self, vertex_a, vertex_b, weight=1.0):
        self.edge_weights[(vertex_a, vertex_b)] = weight


# Reads in the distance table file and inserts the address into the delivery list
# Insert a new edge between addresses
# STC: O(n^2)
def delivery_graph():
    packageEdges = Graph()
    address = []
    with open('../WGUPS/WGUPSDistanceTable.csv') as csvFile:
        readCSV = csv.reader(csvFile, delimiter=',')
        for row in readCSV:
            address.append(row)
        for row in address:
            packageEdges.add_vertex(row[1])

        for row in address:
            for i in range(3, len(row)):
                packageEdges.add_new_edge(row[1], address[i - 3][1], float(row[i]))

        return packageEdges


# Sets distance_graph to the dictionary of edge weights
distance_graph = delivery_graph()
