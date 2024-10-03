from account import Account

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder, initial_balance=0):
        self.accounts[account_number] = Account(account_number, account_holder, initial_balance)

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            return account.deposit(amount)
        return False

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            return account.withdraw(amount)
        return False

    def get_balance(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            return account.get_balance()
        return None

    def get_account_holder(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            return account.account_holder
        return None

    def get_all_accounts(self):
        return [str(account) for account in self.accounts.values()]
