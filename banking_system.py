#Create the Main menu
def show_menu():
    print("\n------------------------------")
    print("WELCOME TO OUR BANK")
    print("Choose an option to Continue")
    print("------------------------------")
    print("\n1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. View All Accounts")
    print("6. View Transactions")
    print("7. Exit\n")

#Load accounts
def load_accounts():
    try:
        with open("account.json", "r") as file:
            accounts = file.load(file)
            return accounts
    except FileNotFoundError:
        return
    
#Find account
def find_account(accounts, name):
    for account in accounts:
        if account ["name"].lowe() == name.lower:
            return account
    return ("No such account found. Back to menu to create account")

#Create account function   
def create_account(accounts):
    name = input("Enter the account name: ") #Ask the user to enter the account name.
    
    if name.strip() == "":
        print("Account name cannot be empty.")
        return
        existing_account = find_account(account, name)

        if existing_account:
            print("Account with this name already exist")
        else:
            new_account={
                "name": name,
                "balance":0,
                "transactions": []
            }
#Deposit money function   
def deposit_money(accounts):
    name = input("Ente the account name: ")
    
#Withdraw money function   
def withdraw_money(accounts):
    name = input("Ente the account name: ")

#Check balance function    
def check_balance(accounts):
    name = input("Ente the account name: ")

#View all accounts function    
def view_accounts(accounts):
    name = input("Ente the account name: ")
#View all transactions function   
def view_transactions(accounts):
    name = input("Ente the account name: ")
    
def main():
    accounts = load_accounts()

    while True:
        show_menu()

        choice = input("Choose an option: ")

        if choice == "1":
            create_account(accounts)

        elif choice == "2":
            deposit_money(accounts)

        elif choice == "3":
            withdraw_money(accounts)

        elif choice == "4":
            check_balance(accounts)

        elif choice == "5":
            view_accounts(accounts)

        elif choice == "6":
            view_transactions(accounts)

        elif choice == "7":
            print("Thank you for using the bank app")
            break

        else:
            print("Invalid option. Please choose from 1 to 7")
            
main()