from BankAccount import BankAccount


class CurrentAccount(BankAccount):

    # CurrentAccount put 200INR as charges on each withdrawal
    def withdraw(self, amount):
        print('200 INR charges will be included for your every withdrawal')
        if super().withdraw(amount + 200) == 1:
            return 1

