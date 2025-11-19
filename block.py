import hashlib
import json
import time
import random

class Block:

    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.timestamp = time.time()
        self.nonce = 0
        self.merkle_root = compute_merkle_root(transactions)
        self.hash = self.compute_hash()

    def header_dict(self):
        return {
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp,
            "nonce": self.nonce,
            "merkle_root": self.merkle_root,
        }

    def compute_hash(self):
        header_json = json.dumps(self.header_dict(), sort_keys=True)
        return sha256(header_json)

        #Simple Proof-of-Work: find nonce so hash starts with '000'
    def mine(self, difficulty=3):
        target = "0" * difficulty
        while True:
            h = self.compute_hash()
            if h.startswith(target):
                self.hash = h
                return h
            self.nonce += 1




def sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()


def generate_address():
    #Generate a blockchain-like 40-hex-character address
    return "0x" + "".join(random.choice("0123456789abcdef") for _ in range(40))


def compute_merkle_root(transactions):
    if not transactions:
        return "0" * 64

    level = [sha256(tx) for tx in transactions]

    while len(level) > 1:
        new_level = []
        for i in range(0, len(level), 2):
            left = level[i]
            right = level[i + 1] if i + 1 < len(level) else left
            new_level.append(sha256(left + right))
        level = new_level

    return level[0]
