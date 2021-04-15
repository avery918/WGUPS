from Distance import distance_graph

# This is a greedy algorithm that first takes  truck route as a parameter
# Creates a new list with the hub as the starting location
# As the algorithm loops through the truck route it takes the smallest edge weight and appends the second of the two
# addresses to the new list
# It also removes that address from the truck route
# The algorithm will always append the address that produces the smallest edge weight at the current time
# After the truck route is empty the new truck route of shortest distance travel is returned
# STC: O(n^2)
def shortTravelDistance(truckRoute):
    currentRoute = []
    shortestRoute = ["4001 South 700 East"]
    distances = distance_graph.edge_weights
    i = 0

    for row in truckRoute:
        currentRoute.append(row)

    while len(currentRoute) > 0:
        nextStop = ""
        milesToStop = 25.0

        for route in currentRoute:
            currentMile = distances[shortestRoute[i], route]
            if currentMile < milesToStop:
                milesToStop = currentMile
                nextStop = route

        shortestRoute.append(nextStop)
        currentRoute.remove(nextStop)

        i += 1

    return shortestRoute

