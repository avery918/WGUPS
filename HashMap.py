class HashTable:
    # HashTable constructor.
    # The space time complexity is O(1)
    def __init__(self, capacity=10):
        # initialize the hash table with empty bucket list entries.
        self.hashMap = []
        for i in range(capacity):
            self.hashMap.append([])

    # Adds new package into table.
    # The space time complexity is O(1)
    def insert(self, key, value):
        keyHash = int(key) % len(self.hashMap)
        keyValue = [key, value]
        if value[7] != 'Delayed9:05':
            value.append("At the Hub")

        else:
            value.append("Delivery Delayed - At Hub")
        self.hashMap[keyHash].append(value)

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    # The space time complexity is O(N)
    def getPackage(self, key):
        # get the bucket list where this key would be.
        keyHash = int(key) % len(self.hashMap)
        bucketList = self.hashMap[keyHash]
        print(keyHash)
        # search for the key in the bucket list
        for keyValue in bucketList:
            if keyValue[0] == key:
                return keyValue
        # the package was not found .
        return None

    # Removes an item with matching key from the hash table.
    # The space time complexity is O(N)
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        keyHash = int(key) % len(self.hashMap)
        bucketList = self.hashMap[keyHash]

        for keyValue in bucketList:
            if key in bucketList:
                bucketList.remove(key)

    # Checks to see if a package is in the hash table and make the necessary updates to the package
    # Returns true i package is found, false otherwise
    # The space time complexity is O(N)
    def updatePackage(self, key, value):
        keyHash = int(key) % len(self.hashMap)
        if self.hashMap[keyHash] is not None:
            for kv in self.hashMap[keyHash]:
                if kv[0] == key:
                    kv = value
                    return True
        else:
            return False

