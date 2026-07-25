class Account:
    def init(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

    def statement(self):
        print(f"{self.owner} | {self.account_number} | Balance: {self.balance} ETB")


class SavingsAccount(Account):
    def __init(self, owner, account_number, balance=0, rate=0.05):
        super().init(owner, account_number, balance)
        self.rate = rate

    def add_interest(self):
        interest = self.balance * self.rate
        self.deposit(interest)

    def statement(self):
        print(f"[Savings] {self.owner} | {self.account_number} | Balance: {self.balance:.2f} ETB")


class CurrentAccount(Account):
    def init(self, owner, account_number, balance=0, overdraft=1000):
        super().init(owner, account_number, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self.balance + self.overdraft:
            raise ValueError("Over limit")

        self._Account__balance -= amount

    def statement(self):
        print(f"[Current] {self.owner} | {self.account_number} | Balance: {self.balance:.2f} ETB")


# Polymorphism
accounts = [
    SavingsAccount("Almaz", "CBE-001", 1500),
    CurrentAccount("Dawit", "CBE-002", 800)
]

for acc in accounts:
    acc.deposit(100)

    if isinstance(acc, SavingsAccount):
        acc.add_interest()

    acc.statement()