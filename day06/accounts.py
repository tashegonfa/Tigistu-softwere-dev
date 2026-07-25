class Account:
    def init(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance
        self._observers = []
    @property
    def balance(self):
        return self.__balance
    def subscribe(self, observer):
        self._observers.append(observer)
    def _notify(self, event):
        for observer in self._observers:
            observer.update(event)
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.__balance += amount
        self._notify(f"{self.owner} deposited {amount} ETB")
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        self._notify(f"{self.owner} withdrew {amount} ETB")
    def statement(self):
        print(f"{self.owner} | {self.account_number} | Balance: {self.balance:.2f} ETB")

class SavingsAccount(Account):

    def __init(self, owner, account_number, balance=0, rate=0.05):
        super().init(owner, account_number, balance)
        self.rate = rate
    def add_interest(self):
        interest = self.balance * self.rate
        self.deposit(interest)


class CurrentAccount(Account):

    def init(self, owner, account_number, balance=0, overdraft=1000):
        super().init(owner, account_number, balance)
        self.overdraft = overdraft
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.balance + self.overdraft:
            raise ValueError("Overdraft limit exceeded")
        self._Account__balance -= amount
        self._notify(f"{self.owner} withdrew {amount} ETB")
# Main program
if name == "main":
    acc = SavingsAccount("Almaz", "001", 1000)
    acc.deposit(500)
    acc.statement()