from bank import Bank
from account import Account

def load_accounts_from_file(bank, filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Remove leading/trailing spaces and ensure it's not an empty line
                line = line.strip()
                if line:
                    data = line.split(',')
                    if len(data) == 3:
                        account_number, account_holder, initial_balance = data
                        bank.create_account(account_number.strip(), account_holder.strip(), float(initial_balance.strip()))
                    else:
                        print(f"Skipping invalid line: {line}")
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    bank = Bank()

    # Load accounts from data.txt
    load_accounts_from_file(bank, 'data.txt')

    # Dynamic Deposit
    account_to_deposit = input("Enter account number to deposit: ")
    deposit_amount = float(input("Enter deposit amount: "))
    if bank.deposit(account_to_deposit, deposit_amount):
        print(f"Successfully deposited {deposit_amount} to account {account_to_deposit}.")
    else:
        print(f"Deposit failed for account {account_to_deposit}.")

    # Dynamic Withdrawal
    account_to_withdraw = input("\nEnter account number to withdraw from: ")
    withdrawal_amount = float(input("Enter withdrawal amount: "))
    
    if bank.withdraw(account_to_withdraw, withdrawal_amount):
        print(f"Successfully withdrew {withdrawal_amount} from account {account_to_withdraw}.")
    else:
        print(f"Withdrawal failed for account {account_to_withdraw}.")

    # Balance inquiries
    account_to_check = input("\nEnter account number to check balance: ")
    balance = bank.get_balance(account_to_check)
    account_holder = bank.get_account_holder(account_to_check)

    if balance is not None:
        print(f"Account Holder: {account_holder}\nAccount No: {account_to_check}\nBalance: {balance}")
    else:
        print(f"Account {account_to_check} does not exist.")

if __name__ == "__main__":
    main()
