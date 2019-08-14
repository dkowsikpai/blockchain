
class NewBlock():
    # Creating a new Block Chain using the  following data. Index, Data, and timestamp
    def __init__(self, index, data, timestamp, previousHash):
        # Individual Block data
        self.index = index
        self.data = data
        self.timestamp = timestamp
        # Hash of the previous block in the block chain
        self.previousHash = previousHash
        # Calculating the hash of the current block with the ceaser cypher algorithm, Hash changes if the data of the block changes
        self.hash = self.encrypt(str(index)+str(data)+str(timestamp))

    def encrypt(self, text):
        # Ceaser Cypher algorithm
        s = len(text)
        result = ""
        # transverse the plain text
        for i in range(len(text)):
            char = text[i]
            # Encrypt uppercase characters in plain text
            if (char.isupper()):
                result += chr((ord(char) + s-65) % 26 + 65)
                # Encrypt lowercase characters in plain text
            else:
                result += chr((ord(char) + s - 97) % 26 + 97)
        return result


    def printBlock(self):
        # returning the block data in form of the dictionary
        dic = {"index:": str(self.index), "Data: ": self.data, "Time Stamp: ": str(self.timestamp), "Previous Hash: ": self.previousHash, "Hash: ": self.hash}
        return dic
    


class BlockChain(NewBlock):
    # Class/Model to create a blockchain object each block chain object is a advanced form of the doubly linked list (2 directional linked list)
    def __init__(self):
        # initial block of the block chain is the genisis block and the previousHash is 0, It is like a header/root of the linked list
        self.chain = [NewBlock(0, "1/1/2018", "Genisis", 0)]

    def addBlock(self, index, data, timestamp):
        # Adding new block to the block chain. It is simple addition we have to first run the validBlock to add the Block
        if self.validBlock():
            self.chain.append(NewBlock(index, data, timestamp, self.chain[-1].hash))
            # printing the chain after the addition of the new block
            # print(self.chain)

    def validBlock(self):
        # Funtion to check whether the block chain is tampered or NOT
        for i in range(1, len(self.chain)):
            if not self.chain[i].hash == self.chain[i].encrypt(str(self.chain[i].index)+str(self.chain[i].data)+str(self.chain[i].timestamp)):
                return False
            if self.chain[i-1].hash != self.chain[i].previousHash :
                return False
        return True

    def __str__(self):
        return self.chain


# temp is the blockchain object
temp = BlockChain()
temp.addBlock(1, "csdszd", "2/1/2018")
temp.addBlock(2, "zss", "3/1/2018")
# Some manipulation of the blockchain
for i in temp.chain:
    print(i.printBlock())
print(temp.validBlock())

# Addind a blck and checking the validity of the blockchain
temp.addBlock(3, "nskcnsz", "4/1/2018")
for i in temp.chain:
    print(i.printBlock())

# Tampering of the block manually
temp.chain[1].index = 3
temp.chain[1].hash = temp.encrypt(str(temp.chain[1].index)+str(temp.chain[1].data)+str(temp.chain[1].timestamp))
print(temp.validBlock())

# After tampering data no Blocks can be added to the invalid blockchain
temp.addBlock(4, ",sndk", "5/1/2018")
for i in temp.chain:
    print(i.printBlock())
