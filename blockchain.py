from block import *




class Blockchain:
    def __init__(self, difficulty=3):
        self.chain = []
        self.difficulty = difficulty
        self.create_genesis_block()

    def create_genesis_block(self):
        tx = ["[SYSTEM] --> [" + generate_address() + "] : [50 yfc]"]
        genesis = Block(0, tx, "0" * 64)
        genesis.mine(self.difficulty)
        self.chain.append(genesis)

    def last_block(self):
        return self.chain[-1]

    def create_transaction(self, sender, receiver, amount, unit="yfc"):

        return f"[{sender}] --> [{receiver}] : [{amount} {unit}]"

    def add_block(self, transactions):
        block = Block(
            index=len(self.chain),
            transactions=transactions,
            previous_hash=self.last_block().hash
        )
        block.mine(self.difficulty)
        self.chain.append(block)
        return block

    def display(self):
        print("=" * 90)
        print("BLOCKCHAIN")
        print("=" * 90)
        for b in self.chain:
            print(f"Block #{b.index}")
            print(" Header:")
            print(f"   Previous Hash : {b.previous_hash}")
            print(f"   Timestamp     : {time.ctime(b.timestamp)}")
            print(f"   Nonce         : {b.nonce}")
            print(f"   Merkle Root   : {b.merkle_root}")
            print(f"   Block Hash    : {b.hash}")
            print(" Body (Transactions):")
            for tx in b.transactions:
                print(f"     • {tx}")
            print("-" * 90)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            cur = self.chain[i]
            prev = self.chain[i - 1]

            if cur.previous_hash != prev.hash:
                print(f"Block {i}: broken previous_hash link")
                return False

            if cur.merkle_root != compute_merkle_root(cur.transactions):
                print(f"Block {i}: Merkle root mismatch")
                return False

            if cur.hash != cur.compute_hash():
                print(f"Block {i}: hash mismatch")
                return False

        print("Blockchain valid")
        return 1

