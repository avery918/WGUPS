import csv
from HashMap import HashTable

with open('WGUPS_Package.csv') as csvFile:
    readCSV = csv.reader(csvFile, delimiter=',')

    addToHash = HashTable()
    truck1 = []
    truck2 = []
    truck3 = []
    truck1Route = []
    truck2Route = []
    truck3Route = []

    # For loop retrieves the rows of data from the csvFile and cycles through them
    # As it cycles through the rows, it adds each row to a particular truck depending on requirements
    # At end of each cycle row is inserted in haspMap
    # STC: O(n)

    for row in readCSV:

        # Each row appended to end of truck list in which it meets the criteria
        # rows that do now meet any criteria are appended to truck 3 which is used to hold each packages

        if row[5] == "9:00 AM":
            truck1.append(row)
            truck1Route.append(row[1])
        elif row[5] != "EOD" and ("84119" not in  row[4] and "84111" not in row[4]) and ("deliver" in row[7] or "n/a" in row[7]):
            truck1.append(row)
            truck1Route.append(row[1])
        elif "84106" in row[4]:
            truck1.append(row)
            truck1Route.append(row[1])
        elif row[5] != "EOD" or "84104" in row[4]:
            truck2.append(row)
            truck2Route.append(row[1])
        elif "Delayed9:05" in row[7] or "truck2" in row[7]:
            truck2.append(row)
            truck2Route.append(row[1])

        elif row[7] == "Wrong":
            truck3.append(row)

            truck3Route.append(row[1])
        elif "84115" in  row[4]:
            truck1.append(row)
            truck1Route.append(row[1])

        else:
            truck3.append(row)
            truck3Route.append(row[1])
        addToHash.insert(row[0],row)

    # Appends the starting times of each truck to the packages that are associated with that truck
    # The space time complexity is O(N)

    for row in truck1:
        row.append("8:00 AM")
        row.append("")
    for row in truck2:
        row.append("9:10 AM")
        row.append("")
    for row in truck3:
        row.append("11:00 AM")
        row.append("")

    def getAddToHash():
        return addToHash

    # Returns all packages on the first truck
    # STC: O(1)
    def getTruck1():
        return truck1


    # Returns all packages on the second truck
    # STC: O(1)
    def getTruck2():
        return truck2


    # Returns all packages on the third truck
    # STC: O(1)
    def getTruck3():
        return truck3


    # Return route for first truck
    # STC: O(1)
    def getTruck1Route():
        return truck1Route


    # Return route for second truck
    # STC: O(1)
    def getTruck2Route():
        return truck2Route


    # Return route for third truck
    # STC: O(1)
    def getTruck3Route():
        return truck3Route

    # Is passed a package Id to look up. Return package info if package is found otherwise returns None
    # The space time complexity is O(N)
    def lookUpPackage(packageId):
        reu = getAddToHash()
        packageInfo = reu.getPackage(packageId)

        return packageInfo