class BankAccount:
    # current Balance variable is to store the available balance
    __currentBalance = None

    # Constructor for this class BankAccount when object is created
    def __init__(self, amount):
        # assigning value to the private variables
        self.__currentBalance = amount
        print('Your account is successfully created ... :)')

    # This deposit method is used to increment the available balance with the current deposited amount
    def deposit(self, amount):
        self.__currentBalance += amount
        # Acknowledgment of deposition
        print('Deposit of amount '+str(amount) + ' INR is successfully credited to your account ')

    # This withdraws method is used decrement withdrawal amount from current available balance
    def withdraw(self, amount):
        # Checking the requested amount is greater than the balance amount
        if amount > self.__currentBalance:
            print('You are unable to withdraw amount please check your balance..')

        # If requested amount is not greater than the available balance
        else:
            self.__currentBalance -= amount
            print('Amount '+str(amount) + ' INR is debited from your Account')
            return 1

    # check_balance method is displays the balance in account
    def check_balance(self):
        print('your balance amount is ..'+str(self.__currentBalance)+' INR')

    # This method is used to transfer the amount from one account to another account
    def transfer(self, amount, ac):
        # if statement here is used confirm the Withdrawal of sender account and verifying amount is greater than zero
        if self.withdraw(amount) == 1:
            print('Transacting....')
            print('Transfer of amount is confirmed')
            ac.deposit(amount)


