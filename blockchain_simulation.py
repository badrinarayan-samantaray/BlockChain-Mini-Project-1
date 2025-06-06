import hashlib
import time

# Block structure
class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.ctime()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()
    # Implement hash generator using SHA256
    def calculate_hash(self):
        block_string = str(self.index) + self.timestamp + self.data + self.previous_hash + str(self.nonce)
        return hashlib.sha256(block_string.encode()).hexdigest()

# Blockchain with 3 blocks
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), data, previous_block.hash)
        self.chain.append(new_block)

    def print_chain(self):
        for block in self.chain:
            print(f"Block {block.index}:\nData: {block.data}\nHash: {block.hash}\nPrevious: {block.previous_hash}\n")
    #Tamper & Recalculate hash 
    def tamper_demo(self):
        #Demonstrates how tampering breaks the chain.
        print("Performing Tampering")
        print("Original Chain:")
        self.print_chain()

        print("Tampering with Block 1's data -")
        self.chain[1].data = "Badrinarayan Samantaray"
        self.chain[1].hash = self.chain[1].calculate_hash()

        print("Chain After Tampering:")
        self.print_chain()
        print("Notice: Block 2's 'previous_hash' no longer matches Block 1's hash!")

# Display
my_chain = Blockchain()
my_chain.add_block("Block 1 Data")
my_chain.add_block("Block 2 Data")


my_chain.print_chain()
my_chain.tamper_demo()

