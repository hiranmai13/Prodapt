import banking.accounts as acc

def deposit(amount):
    acc.balance += amount
def withdraw(amount):
    acc.balance -= amount