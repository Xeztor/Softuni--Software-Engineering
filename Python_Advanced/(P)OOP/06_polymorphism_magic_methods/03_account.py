class Account(object):
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, item):
        return self._transactions[item]

    def __reversed__(self):
        return reversed(self._transactions)

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __add__(self, other):
        new_account = Account(f"{self.owner}&{other.owner}", self.amount)
        new_account_transactions = self._transactions.copy()
        new_account_transactions.extend(other._transactions)
        new_account._transactions = new_account_transactions

        return new_account

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")

        self._transactions.append(amount)

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    def validate_transaction(self, amount_to_add):
        if self.balance + amount_to_add < 0:
            raise ValueError("sorry cannot go in debt!")

        self.add_transaction(amount_to_add)
        return f"New balance: {self.balance}"


acc = Account('lazar', 20)
print(acc.balance)
print(acc.owner)
print(acc.add_transaction(-30))
print(acc.balance)

# acc = Account('bob', 10)
# acc2 = Account('john')
# print(acc)
# print(repr(acc))
# acc.add_transaction(20)
# acc.add_transaction(-20)
# acc.add_transaction(30)
# print(acc.balance)
# print(len(acc))
# for transaction in acc:
#     print(transaction)
# print(acc[1])
# print(list(reversed(acc)))
# acc2.add_transaction(10)
# acc2.add_transaction(60)
# print(acc > acc2)
# print(acc >= acc2)
# print(acc < acc2)
# print(acc <= acc2)
# print(acc == acc2)
# print(acc != acc2)
# acc3 = acc + acc2
# print(acc3)
# print(acc3._transactions)
