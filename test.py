from conta import Account

account = Account(123, "Nico", 55.0, 1000.0)
account2 = Account(321, "MArco", 100.0, 1000.0)

account.transfer(account2, 5000)

account2.extract()
account.withdraw(1100)
account.extract()

account.limit = 15000
print(account.limit)

print(Account.bank_code())