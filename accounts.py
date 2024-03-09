import datetime
import random

class BasicAccount:
    """
    Represents a person's basic bank account.

    Attributes:
        name (string): the name of the account holder.
        ac_num (int): stores the number of the account, with the first account being 1.
        balance (float): stores the balance of the account.
        card_num (string): for storing a new card number as a 16 character string.
        card_exp (tuple(int, int)): for storing a new expiry data in (MM, YY) format.
        ac_num_class_variable (int): a class variable for incrementing the account numbers.
        ovedraft_limit (int): tells the program that a basic account has no overdraft.

    Methods:
        __init__(self, ac_name, opening_balance):
            Initialises the instance of the class.
        __str__(self):
            Returns a string with the account name, available balance and if there is an overdraft.
        deposit(self, amount):
            Deposits money into the account.
        withdraw(self, amount):
            Withdraws money from the account.
        get_available_balance(self):
            Returns the total balance plus any overdraft.
        get_balance(self):
            Returns the balance not including any overdraft.
        print_balance(self):
            Prints the balance of the account.
        get_name(self):
            Returns the account holder's name.
        get_ac_num(self):
            Returns the account's account number.
        issue_new_card(self):
            Issues a new card with a 16-digit card number and expiry date 3 years to the month from now.
        close_account(self):
            Closes the account by withdrawing all money via the withdraw method.
    """

    ac_num_class_variable = 1

    def __init__(self, ac_name, opening_balance):
        """
        This function initialises the BasicAccount class.
        It increments the account number.
        It stores the card number and card expiry date.

        Parameters:
            ac_name (str): the account's name.
            opening_balance (float): the opening balance of an account.
        Returns:
            Nothing
        """
        self.name = ac_name
        self.balance = float(opening_balance)
        self.ac_num = BasicAccount.ac_num_class_variable
        BasicAccount.ac_num_class_variable += 1
        self.card_num = "0000000000000000"
        self.card_exp = (00, 00)
        self.overdraft_limit = 0

    def __str__(self):
        """
        Returns a string with the account name, available balance and if there is an overdraft.

        Parameters:
            None
        Returns:
            (str): a string with information about the account.
        """
        return f"The account name is {self.name}. The available balance is £{self.balance:.2f}. There is no overdraft facility as this is a Basic Account."

    def deposit(self, amount):
        """
        Deposits money into an account.
        Adjusts the account balance accordingly.
        Validates if the amount entered is positive.

        Parameters:
            amount (float): a positive amount to deposit.
        Returns:
            None
        """
        try:
            if float(amount) > 0:
                self.balance = self.balance + amount
            else:
                print("Please enter a positive decimal amount.")
        except ValueError:
            print("Please enter a positive decimal amount.")

    def withdraw(self, amount):
        """
        Withdraws money from an account.
        Prints a message stating who has withdrawn money, how much and the new balance.
        Prints if an amount can not be withdrawn.
        For a Premium Account it takes into account an overdraft when looking at someone's balance.
        Validates if the amount entered is positive.

        Parameters:
            amount (float): a positive amount to withdraw.
        Returns:
            None
        """
        try:
            # The if statement checks if the amount is > 0.
            # This also checks if the amount to be withdrawn is less than the balance plus any overdraft.
            if float(amount) > 0 and float(amount) <= (self.balance + float(self.overdraft_limit)):
                self.balance = self.balance - amount
                print(f"{self.name} has withdrawn £{amount}. New balance is £{self.balance:.2f}.")
            elif float(amount) > self.balance:
                print(f"Can not withdraw £{amount}.")
            else:
                print("Please enter a positive decimal.")
        except ValueError:
            print("Please enter a positive decimal.")

    def get_available_balance(self):
        """
        Gives the total balance available in an account.
        Takes into account any overdraft when doing this.

        Parameters:
            None
        Returns:
            total_balance (float): the account's total balance in pounds.
        """
        total_balance = float(self.balance)
        return total_balance

    def get_balance(self):
        """
        Gives the balance of an account.
        The balance will be negative if an account is overdrawn.

        Parameters:
            None
        Returns:
            balance (float): the account's balance in pounds.
        """
        return self.balance

    def print_balance(self):
        """
        Prints the balance of an account.

        Parameters:
            None
        Returns:
            None
        """
        print(f"The balance of the account is £{self.balance:.2f}.")

    def get_name(self):
        """
        Gives the name of an account's holder.

        Parameters:
            None
        Returns:
            account_holder (str): the name of the account's holder.
        """
        return str(self.name)

    def get_ac_num(self):
        """
        Gives an account's number.

        Parameters:
            None
        Returns:
            ac_num (str): the account's account number.
        """
        return str(self.ac_num)

    def issue_new_card(self):
        """
        Makes a new card number to expire 3 years to the month from the current date.
        Firstly, creates a new random 16-digit account number.
        Secondly, creates an expiry date three years from now in (MM, YY) format.

        Parameters:
            None
        Returns:
            None
        """
        self.card_num = str(random.randint(0, 9))
        while len(self.card_num) < 16:
            new_number = random.randint(0, 9)
            self.card_num = str(self.card_num) + str(new_number)
        current_date = datetime.datetime.now()
        card_exp_year = int(current_date.strftime("%y")) + 3
        self.card_exp = (int(current_date.strftime("%m")), int(card_exp_year))

    def close_account(self):
        """
        Withdraws any balance to the customer (via the withdraw method), then it returns True.
        If the the customer is in debt, it prints a message, then it return False.

        Parameters:
            None
        Returns:
            True or False (Boolean): True if the account can be closed, False if not.
        """
        if self.balance == 0:
            return True
        else:
            self.withdraw(self.balance)
            return True

class PremiumAccount(BasicAccount):
    """
    Represents a person's premium bank account.

    Attributes:
        overdraft (boolean): whether the account has an overdraft or not. If yes then True, if no then False.
        overdraft_limit (float): the limit of the overdraft of an account. This is £0 if there is not one.

    Methods:
        __init__(self, ac_name, opening_balance, initial_overdraft):
            Initialises the instance of the class. Override the BasicAccount method.
        __str__(self):
            Provides a string with the account name, available balance and if there is an overdraft. Override the BasicAccount method.
        set_overdraft_limit(self, new_limit):
            Sets the overdraft limit for the account.
        get_available_balance(self):
            Returns the total balance plus any overdraft. Override the BasicAccount method.
        print_balance(self):
            Prints the balance of the account, the overdraft limit and the available overdraft. Override the BasicAccount method.
        close_account(self):
            Checks if the account can be closed, closes the account by withdrawing all money via the withdraw method. Override the BasicAccount method.
    """

    def __init__(self, ac_name, opening_balance, initial_overdraft):
        """
        A function to initiate the class.

        Parameters:
            ac_name (str): the account's name (from BasicAccount __init__ method).
            opening_balance (float): the opening balance of the account (from BasicAccount __init__ method).
            initial_overdraft (float): the initial overdraft of the account (0 or above).
        Returns:
            None
        """
        super().__init__(ac_name, float(opening_balance))
        self.overdraft = True
        if initial_overdraft == 0:
            self.overdraft = False
        else:
            self.overdraft = True
        self.overdraft_limit = float(initial_overdraft)

    def __str__(self):
        """
        Returns a string with the account name, available balance and if there is an overdraft.

        Parameters:
            None
        Returns:
            (str): a string with information about the account.
        """
        return f"The account name is {self.name}. The available balance is £{PremiumAccount.get_available_balance(self):.2f}. There is an overdraft of £{self.overdraft_limit:.2f}."

    def set_overdraft_limit(self, new_limit):
        """
        Sets an account's overdraft limit to the given amount.

        Parameters:
            new_limit (float): the new overdraft limit of the account.
        Returns:
            None
        """
        try:
            if float(new_limit) >= 0:
                self.overdraft_limit = float(new_limit)
            else:
                print("Please enter a positive decimal amount.")
        except ValueError:
            print("Please enter a positive decimal amount.")

    def get_available_balance(self):
        """
        This returns the total balance available in an account.
        It takes into account any overdraft that is available.

        Parameters:
            None
        Returns:
            total_balance (float): the account's total balance in pounds.
        """
        total_balance = float(self.balance) + float(self.overdraft_limit)
        return total_balance

    def print_balance(self):
        """
        Prints the balance of an account.
        States if an overdraft is available.
        The overdraft limit and the remaining overdraft is also printed.

        Parameters:
            None
        Returns:
            None
        """
        if self.balance < 0 and self.overdraft is True:
            remaining_overdraft = self.overdraft_limit + self.balance
            print(f"The balance of the account is £{self.balance:.2f}. An overdraft is available which is £{self.overdraft_limit:.2f}. The overdraft remaining is £{remaining_overdraft:.2f}.")
        elif self.balance >= 0 and self.overdraft is True:
            print(f"The balance of the account is £{self.balance:.2f}. An overdraft is available which is £{self.overdraft_limit:.2f}. The overdraft remaining is £{self.overdraft_limit:.2f}.")
        else:
            print(f"The balance of the account is £{self.balance:.2f}. An overdraft is not available.")

    def close_account(self):
        """
        Withdraws any balance to the customer (via the withdraw method), then it returns True.
        If the the customer is in debt, it prints a message, then it return False.

        Parameters:
            None
        Returns:
            True or False (Boolean): True if the account can be closed.
        """
        if self.balance < 0:
            print(f"Can not close account due to customer being overdrawn by £{(self.balance*-1):.2f}.")
            return False
        # Deals with closing an account where the balance is already £0.00
        elif self.balance == 0:
            return True
        else:
            self.withdraw(self.balance)
            return True
