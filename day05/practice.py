class SavingAccount:
    def calculate_interest(self):
        return 500


class CurrentAccount:
    def calculate_interest(self):
        return 200


def total_interest(accounts):
    total = 0
    for account in accounts:
        total += account.calculate_interest()
    return total


accounts = [SavingAccount(), CurrentAccount()]

print(total_interest(accounts))