import hashlib
import time

class Block:
    def __init__(self, data):
        self.timestamp = time.ctime()
        self.data = data
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        text = self.timestamp + self.data + str(self.nonce)
        return hashlib.sha256(text.encode()).hexdigest()
    # Block Class includes mineBlock(difficulty) function
    def mineBlock(self, difficulty):
        print("Mining block...")
        target = '0' * difficulty # Difficulty set i.e; hash must start with zeros
        start = time.time()
        # Increment the nonce until the hash meets the difficulty condition
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

        end = time.time()
        print(f"Block mined with hash: {self.hash}")
        print(f"Nonce: {self.nonce}")
        print(f"Time taken: {end - start:.2f} seconds")

# Run mining
difficulty = 4  # Difficulty increased to 4 i.e; the hash must start with "0000"
block = Block("Mining this block :")
block.mineBlock(difficulty)
