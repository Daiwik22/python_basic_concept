class Account:
    def __init__(self, name, balance, min_balance):
        self.name=name
        self.balance=balance
        self.min_balance=min_balance

    def deposit(self, amount):
        self.balance+=amount

    def withdraw(self, amount):
        if self.balance-amount>=self.min_balance:
            self.balance-=amount

        else:
            print("Sorry, not enough funds.")

    def statement(self):
        print("Account balance: -> £{}".format(self.balance))

class CurrentAccount(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=200)
    def __str__(self):
        return "{}'s current account £{}".format(self.name, self.balance)

class SavingAccount(Account):
       def __init__(self, name, balance):
            super().__init__(name, balance, min_balance=0)

       def __str__(self):
            return "{}'s current account £{}".format(self.name, self.balance)

Daiwik_account=CurrentAccount("Daiwik", 800)
Daiwik_account.deposit(300)
Daiwik_account.statement()
Daiwik_account.withdraw(2000)
Daiwik_account.statement()