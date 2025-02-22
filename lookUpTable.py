import csv

class LookUpTable():
    def __init__(self, pathToFile = "lookup.csv"):
        self.map = self.getMapping(pathToFile)
    
    def getMap(self):
        return self.map
    
    def getMapping(self, fileName):
        lookup_table = {}
        with open(fileName, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if len(row) != 3:
                    continue
                dstport, protocol, tag = row
                key = (int(dstport), protocol.lower())  # Case-insensitive
                lookup_table[key] = tag
        return lookup_table
