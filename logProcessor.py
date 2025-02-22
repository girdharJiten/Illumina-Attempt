from constants import PROTOCOL_MAP
from collections import defaultdict
from lookUpTable import LookUpTable

class LogProcessor():
    def __init__(self, filePath = "sampleData.txt", isDefaultFormat = True, protocolIndex = 7, dstPortIndex = 6, columnNumber = 14):
        self.path = filePath
        self.isDefault = isDefaultFormat
        self.protocol_index = protocolIndex
        self.dstPort_index = dstPortIndex
        self.maxNumOfValues = columnNumber
        self.outputFileName = "output.txt"
    
    def process(self, lookUpTable):
        if not self.protocol_index or not self.dstPort_index:
            print("Cannot process further without protocol and dstport data, please update logData format")
            return
        if self.dstPort_index >= self.maxNumOfValues or self.protocol_index >= self.maxNumOfValues:
            print("Please enter correct indices for protocol and dstport")
            return
        tag_counts = defaultdict(int)
        port_protocol_counts = defaultdict(int)
        untagged_count = 0
        
        with open(self.path, "r") as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) != self.maxNumOfValues:
                    continue  # Skip invalid lines
                dst_port = int(parts[self.dstPort_index])  # Destination port
                protocol_number = int(parts[self.protocol_index])  # Protocol number
                
                # Map protocol number to name (assuming TCP/UDP/ICMP)
                protocol_name = PROTOCOL_MAP.get(protocol_number, str(protocol_number))
                
                key = (dst_port, protocol_name)
                tag = lookUpTable.get(key, "Untagged")
                
                if tag == "Untagged":
                    untagged_count += 1
                else:
                    tag_counts[tag] += 1
                    port_protocol_counts[key] += 1
        
        # Write output
        with open(self.outputFileName, "a") as file:
            file.write("Tag Counts:\nTag,Count\n")
            for tag, count in sorted(tag_counts.items()):
                file.write(f"{tag},{count}\n")
            file.write(f"Untagged,{untagged_count}\n")
            file.write("\n")
            
            file.write("Port/Protocol Combination Counts:\nPort,Protocol,Count\n")
            for (port, protocol), count in sorted(port_protocol_counts.items()):
                file.write(f"{port},{protocol},{count}\n")
            file.write("\n\n")

if __name__ == "__main__":
    lookupMapping = LookUpTable().getMap()
    print("############# Running default Log case #############")
    lp = LogProcessor().process(lookupMapping)
    print("############# Running custom Log case with correct index mapping #############")
    lp1 = LogProcessor("customData.txt",False, 4,3, 6)
    lp1.process(lookupMapping)
    print("############# Running custome log case with incorrect index mapping #############")
    lp2 = LogProcessor("customData.txt", False, 3,4, 5)
    lp2.process(lookupMapping)
    print("############# Running custome log case with invalid index mapping #############")
    lp3 = LogProcessor("customData.txt", False,4, 5, 2)
    lp3.process(lookupMapping)
