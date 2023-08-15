from BankAccount import BankAccount


class SavingAccount(BankAccount):
    # SavingAccount deposit which provide 3% interest on each deposit
    def deposit(self, amount):
        # calling the deposit method of super class with increment with requested amount(3%)
        print(str(amount*0.03) + ' INR is added to your deposition amount as Interest ')
        super().deposit(amount + amount * 0.03)

