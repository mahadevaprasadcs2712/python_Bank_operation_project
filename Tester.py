from BankAccount import BankAccount
from SavingAccount import SavingAccount
from CurrentAccount import CurrentAccount


class Tester:
    # Creating BankAccounts with initial Balance 500 and 200
    B1 = BankAccount(500)
    B2 = BankAccount(200)
    print('----------------------------------------------------------------------------------------')

    # Withdraw 200 from B1
    B1.withdraw(200)  # B1 300
    print('----------------------------------------------------------------------------------------')
    # Deposit of 1000 in B2
    B2.deposit(1000)  # B2 1200
    print('----------------------------------------------------------------------------------------')

    # Transfer of 500 from B2 to B1
    B2.transfer(500, B1)  # B2 700 and B1 800
    print('----------------------------------------------------------------------------------------')
    # Checking balance in B1 and B2
    B1.check_balance()  # 800
    B2.check_balance()  # 700
    print('----------------------------------------------------------------------------------------')

    # Creating a saving account with initial amount 2000
    S1 = SavingAccount(2000)
    print('----------------------------------------------------------------------------------------')

    # Deposit of 500 in S1
    S1.deposit(500)
    print('----------------------------------------------------------------------------------------')
    # Checking the balance of S1
    S1.check_balance()
    print('----------------------------------------------------------------------------------------')

    # Creating currentAccount
    C1 = CurrentAccount(2000)
    print('----------------------------------------------------------------------------------------')

    # Deposit of 500 in C1
    C1.deposit(500)
    print('----------------------------------------------------------------------------------------')

    # withdraw of 100 from C1
    C1.withdraw(100)
    print('----------------------------------------------------------------------------------------')
    # Transfer 500 to S1
    C1.transfer(500, S1)
    print('----------------------------------------------------------------------------------------')

    # Checking balance amount in S1
    S1.check_balance()

    # Checking balance amount in S1
    C1.check_balance()
    print('----------------------------------------------------------------------------------------')

    # Transfer 500 to C1
    S1.transfer(500, C1)

    print('----------------------------------------------------------------------------------------')

    # Checking balance amount in S1
    S1.check_balance()

    # Checking balance amount in S1
    C1.check_balance()
    print('----------------------------------------------------------------------------------------')
