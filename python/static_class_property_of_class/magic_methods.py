class BankAccount:

    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance

    # Human-readable string representation (for print/logs)
    def __str__(self):
        return f"{self.owner}'s account: ${self.balance}"

    # Developer/Debug representation
    def __repr__(self):
        return f"BankAccount(owner='{self.owner}', balance={self.balance})"

    # Defines '==' equality comparison
    def __eq__(self, other):
        if not isinstance(other, BankAccount):
            return False
        return self.balance == other.balance

    # Allows adding two accounts using '+' operator
    def __add__(self, other):
        return BankAccount(f"{self.owner} & {other.owner}", self.balance + other.balance)

acc1 = BankAccount("Alice", 100)
acc2 = BankAccount("Bob", 200)

print(acc1)             # Alice's account: $100
print(acc1 == acc2)      # False
acc3 = acc1 + acc2
print(acc3)
