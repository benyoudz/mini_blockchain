from blockchain import Blockchain, generate_address



def demo():
    bc = Blockchain(difficulty=3)

    # generate some fake blockchain addresses
    A1 = generate_address()
    A2 = generate_address()
    A3 = generate_address()
    A4 = generate_address()

    tx1 = bc.create_transaction(A1, A2, 150)
    tx2 = bc.create_transaction(A2, A3, 75)
    bc.add_block([tx1, tx2])

    tx3 = bc.create_transaction(A3, A4, 40)
    tx4 = bc.create_transaction(A4, A1, 10)
    tx5 = bc.create_transaction(A4, A1, 10)
    bc.add_block([tx3, tx4, tx5])

    bc.display()
    bc.is_chain_valid()


if __name__ == "__main__":
    demo()
