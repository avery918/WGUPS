# Ryan Boyd Student Id: 001393137
from CSVReader import getTruck3
from CSVReader import getTruck3Route
from CSVReader import lookUpPackage
from Truck import loadAllTrucks
from Truck import allPackageStatuses
from Truck import truckRouteMileage
from Truck import truck1Route
from Truck import truck2Route
from Truck import truck3Route

# The space time complexity for the entire program is O(n^2)

# Loads all of the trucks
loadAllTrucks()


# This function is used as the user interface with the application
def startApplication():
    print("Welcome to WGUPS!")
    menuOptions = "Press 1 to lookup a package\nPress 2 to see all package's statuses" \
                  "\nPress 3 to see mileage data\nPress 0 to exit the system\n"

    currentTime = "7:30 AM"
    print("The current Time: " + currentTime + ". Please choose one of the following options.\n")
    option = input(menuOptions)

    # Continues to loop while the user doesn't selects "0"
    # Based on the selection the user can either see a individual package, see the package status of all packages at a particular time
    # or see current driven mileage for all tucks
    while option != "0":
        # option "1" allow user to look up a package based on package ID
        if option == "1":
            try:
                choice = input("Enter package ID to look up: ")
                packageInfo = lookUpPackage(choice)
                if packageInfo is None:
                    print("Sorry package not found.")
                else:
                    print("\nPackage ID - " + packageInfo[0] + " Information:")
                    print("Address : " + packageInfo[1] + ", " + packageInfo[2] + " " + packageInfo[3] + " " +
                          packageInfo[4] +
                          ", Delivery deadline: " + packageInfo[5] + ", Weight: " + packageInfo[
                              6] + ", Delivery status: " + packageInfo[8]
                          + ", Expected delivery time: " + packageInfo[10] + "\n")

            except ValueError:
                print("\nInvalid input try again.\n")


        # option "2" allows user to see all package statuses at 3 different times of the day
        elif option == "2" and currentTime != "n/a":
            if currentTime == "7:30 AM":
                currentTime = "9:25 AM"
                print("The current time is " + currentTime + ". Truck 1 and 2 are out for deliveries.\n")
                seeStatus = input(
                    "Print status for all package between 8:35 AM and 9:25 AM? Press 1 for yes or any other key for no.\n")
                if seeStatus == "1":
                    allPackageStatuses("9:25")

            elif currentTime == "9:25 AM":
                currentTime = "10:20 AM"
                print("\nThe current time is " + currentTime + ". Error found with package Id 9's delivery "
                                                               "address.\nUpdating information now.")
                packageInfo = lookUpPackage("9")
                getTruck3Route().remove(packageInfo[1])

                getTruck3().remove(packageInfo)
                packageInfo[1] = "410 S State St"
                packageInfo[4] = "84111"

                getTruck3().append(packageInfo)
                getTruck3Route().append(packageInfo[1])
                print("New add is 410 S State St, Salt Lake City, UT 84111\n")
                currentTime = "10:25 AM"

                print("The current time is " + currentTime + ".\n")
                seeStatus = input(
                    "Print status for all package between 9:35 AM and 10:25 AM? Press 1 for yes or any other key for no.\n")
                if seeStatus == "1":
                    allPackageStatuses("10:25")
                currentTime = "11:00 AM"

            elif currentTime == "11:00 AM":
                print("Truck 1 has return to hub. Truck 3 left for deliveries\n")
                seeStatus = input(
                    "Print status for all package between 12:03 PM and 1:12 PM? Press 1 for yes or any other key for no.\n")
                if seeStatus == "1":
                    allPackageStatuses("13:12")
                    currentTime = "n/a"
                    menuOptions = "Press 1 to lookup a package \nPress 3 to see mileage data\nPress 0 to exit the system\n"

        # option "3" allows user to see all of the trucks driven mileage
        elif option == "3":
            truck1mileage = truckRouteMileage(truck1Route)
            truck2mileage = truckRouteMileage(truck2Route)
            truck3mileage = truckRouteMileage(truck3Route)

            print("\nTruck 1 EOD driven mileage = ", "{:.2f}".format(truck1mileage), ".")
            print("Truck 2 EOD driven mileage = ", "{:.2f}".format(truck2mileage), ".")
            print("Truck 3 EOD driven mileage = ", "{:.2f}".format(truck3mileage), ".")

            print("All three trucks EOD mileage = " + str("{:.2f}".format(truck1mileage + truck2mileage + truck3mileage)) + ".\n")



        else:
            print("Invalid selection. Try again.\n")

        option = input(menuOptions)
    print("Thank you for using WGUPS, Have a great day!")

# initial start up of the application
startApplication()

