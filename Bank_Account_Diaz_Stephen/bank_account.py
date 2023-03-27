class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        # don't worry about user info here; we'll involve the User class soon

    def deposit(self, amount):
        self.amount = amount
        self.balance  +=  amount
        print("You deposited $",amount)
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5 
        else: 
            self.balance -= amount 
            print("You withdrew $",amount)
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate 
            print("Yeilded interest is", self.balance)
            return self

    def display_account_info(self):
        print(self.balance) 
        return self 
    

Stephen = BankAccount(0.02, 0) 
Stephen.deposit(2000).deposit(500).deposit(500).withdraw(1000).yield_interest().display_account_info()

David = BankAccount(0.03,0) 
David.deposit(4000).deposit(500).withdraw(200).withdraw(300).withdraw(100).withdraw(300).yield_interest().display_account_info()