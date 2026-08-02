from observer import SMSAlert, AuditLog
from accounts import SavingsAccount
from registry import AccountRegistry

registry = AccountRegistry()
acc1 = AccountFactory.create(
    "savings",
    "Almaz",
    "CBE-001",
    1500
)
acc2 = AccountFactory.create(
    "current",
    "Dawit",
    "CBE-002",
    800
)
registry.add(acc1)
registry.add(acc2)
sms = SMSAlert()
log = AuditLog()
acc1.subscribe(sms)
acc1.subscribe(log)
acc2.subscribe(sms)
acc2.subscribe(log)
acc1.deposit(500)
acc1.withdraw(200)

if isinstance(acc1, SavingsAccount):
    acc1.add_interest()
acc2.deposit(300)
acc2.withdraw(100)

print("\n========== SEARCH ==========")
account = registry.find("CBE-001")
if account:
    account.statement()
print("\n========== HISTORY ==========")
acc1.show_history()
print("\n========== UNDO ==========")
acc1.undo_last()
acc1.statement()
print("\n========== ALL ACCOUNTS ==========")

for account in registry.list_all():
    account.statement()
from factory import AccountFactory