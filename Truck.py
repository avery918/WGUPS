from CSVReader import getTruck1
from CSVReader import getTruck2
from CSVReader import getTruck3
from CSVReader import getTruck1Route
from CSVReader import getTruck2Route
from CSVReader import getTruck3Route
from Distance import distance_graph
from GreedyAlgo import shortTravelDistance
from datetime import datetime
from datetime import timedelta

# Loads each truck with the packages associated with that truck
# The space time complexity is O(1)
truck1 = getTruck1()
truck2 = getTruck2()
truck3 = getTruck3()

# Loads each truck route with the packages addresses associated with that truck
# The space time complexity is O(1)
truck1Route = getTruck1Route()
truck2Route = getTruck2Route()
truck3Route = getTruck3Route()

# Speed used to calculate te minutes it take to go to each address
truckSpeed = 18 / 60


# This function calls the greedy algorithm and returns the new efficient route
# The space time complexity is O(n^2)
def callGreedyAlgorithm(truckRoute):
    newRoute = shortTravelDistance(truckRoute)
    return newRoute


# reloads each of the truck so they match the layout of the new truck route
# STC: O(n^2)
def adjustTruckArrangement(truckRoute, truck):
    newTruck = ["4001 South 700 East"]
    currentTruck = []
    for data in truck:
        currentTruck.append(data)
    for address in truckRoute:
        for info in currentTruck:
            if address == info[1]:
                newTruck.append(info)
                currentTruck.remove(info)
    return newTruck


# Calculates the delivery time of all Packages based on its' trucks start time and appends it to the package information
# STC: O(n2)
def calculateDeliveryTime(hh, mm, truckInfo, truckRoute):
    deliveryTime = datetime(2021, 4, 1, hh, mm)
    edgeWeight = distance_graph.edge_weights

    try:
        for i in range(0, len(truckRoute) - 1):
            distance = edgeWeight[truckRoute[i], truckRoute[i + 1]] / truckSpeed
            deliveryTime += timedelta(minutes=distance)
            delivered = deliveryTime.strftime("%I:%M %p")
            truckInfo[i + 1][10] = delivered

    except IndexError:
        pass


# The initial method that loads each of the trucks
# STC: O(n^2)
def loadAllTrucks():
    getFormatTruck1()
    getFormatTruck2()
    getFormatTruck3()


# Calls the adjustTruckArrangement and calculateDeliveryTime and returns a formatted truck
# STC: O(n^2)
def getFormatTruck1():
    truckRoute = callGreedyAlgorithm(truck1Route)
    formatTruck1 = adjustTruckArrangement(truckRoute, truck1)
    calculateDeliveryTime(8, 00, formatTruck1, truckRoute)

    return formatTruck1


# Calls the adjustTruckArrangement and calculateDeliveryTime and returns a formatted truck
# STC: O(n^2)
def getFormatTruck2():
    truckRoute = callGreedyAlgorithm(truck2Route)
    formatTruck2 = adjustTruckArrangement(truckRoute, truck2)
    calculateDeliveryTime(9, 10, formatTruck2, truckRoute)
    return formatTruck2


# Calls the adjustTruckArrangement and calculateDeliveryTime and returns a formatted truck
# STC: O(n^2)
def getFormatTruck3():
    truckRoute = callGreedyAlgorithm(truck3Route)
    formatTruck3 = adjustTruckArrangement(truckRoute, truck3)
    calculateDeliveryTime(10, 45, formatTruck3, truckRoute)
    return formatTruck3


# This function prints out the package statuses of each of the truck at a give time
# Updates package status based on selected time
# STC: O(n)
def allPackageStatuses(currentTme):
    truck1 = getFormatTruck1()
    truck2 = getFormatTruck2()
    truck3 = getFormatTruck3()
    truck1mileage = 0
    truck2mileage = 0
    truck3mileage = 0

    timeToCompare = datetime.strptime(currentTme, "%H:%M")

    print("\n\t\t\t\t\t\t\t\t\t\tTruck 1 delivery status:\n=================================================="
          "=================================================================")
    for i in range(1, len(truck1)):
        if datetime.strptime(truck1[i][9], "%H:%M %p") < timeToCompare:
            if timeToCompare > datetime.strptime(truck1[i][10], "%H:%M %p"):
                truck1[i][8] = "Delivered"
            else:
                truck1[i][8] = "Out for delivery"

        print(
            "Package ID  " + truck1[i][0] + " - Address : " + truck1[i][1] + ", " + truck1[i][2] + " " + truck1[i][4] +
            ", Delivery deadline: " + truck1[i][5] + ", Weight: " + truck1[i][6] + ", Delivery status: " +
            truck1[i][8]
            + ", Delivery time: " + truck1[i][10] + "\n")
    truck1mileage += truckRouteMileage(truck1Route)
    print("Truck 1 EOD mileage = ", "{:.2f}".format(truck1mileage))

    print("\n\t\t\t\t\t\t\t\t\t\tTruck 2 delivery status:\n=================================================="
          "=================================================================")
    for i in range(1, len(truck2)):
        if datetime.strptime(truck2[i][9], "%H:%M %p") < timeToCompare:
            if timeToCompare > datetime.strptime(truck2[i][10], "%H:%M %p"):
                truck2[i][8] = "Delivered"
            else:
                truck2[i][8] = "Out for delivery"
        print("Package ID  " + truck2[i][0] + " - Address: " + truck2[i][1] + ", " + truck2[i][2] + " " + truck2[i][4] +
              ", Delivery deadline: " + truck2[i][5] + ", Weight: " + truck2[i][6] + ", Delivery status: " +
              truck2[i][8]
              + ", Delivery time: " + truck2[i][10] + "\n")

    truck2mileage += truckRouteMileage(truck2Route)
    print("Truck 2 EOD mileage = ", "{:.2f}".format(truck2mileage))

    print("\n\t\t\t\t\t\t\t\t\t\tTruck 3 delivery status:\n=================================================="
          "=================================================================")

    for i in range(1, len(truck3)):
        if datetime.strptime(truck3[i][9], "%H:%M %p") < timeToCompare:
            if timeToCompare > datetime.strptime(truck3[i][10], "%H:%M %p"):
                truck3[i][8] = "Delivered"
            else:
                truck3[i][8] = "Out for delivery"
        print("Package ID  " + truck3[i][0] + " - Address: " + truck3[i][1] + ", " + truck3[i][2] + " " + truck3[i][4] +
              ", Delivery deadline: " + truck3[i][5] + ", Weight: " + truck3[i][6] + ", Delivery status: " +
              truck3[i][8]
              + ", Delivery time: " + truck3[i][10] + "\n")
    truck3mileage += truckRouteMileage(truck3Route)
    print("Truck 3 EOD mileage = ", "{:.2f}".format(truck3mileage), "\n")



# Calculates each of the trucks driven mileage
# STC: O(n)
def truckRouteMileage(truckRoute):
    totalMileage = 0
    edgeWeights = distance_graph.edge_weights
    t = shortTravelDistance(truckRoute)
    try:
        for i in range(0, len(edgeWeights) - 1):
            totalMileage += edgeWeights[t[i], t[i + 1]]
    except IndexError:
        pass
    return totalMileage
