import json
import os

FILE_NAME = "balance.json"

def load_balance():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            data = json.load(f)
            return data["balance"]
    return 0

def save_balance(balance):
    with open(FILE_NAME, "w") as f:
        json.dump({"balance": balance}, f)

balance = load_balance()

while True:
    print("\n--- Simple Bank ---")
    print(f"Current balance: ${balance}")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Amount to deposit: $"))
        balance += amount
        save_balance(balance)
        print(f"Deposited ${amount}. New balance: ${balance}")

    elif choice == "2":
        amount = float(input("Amount to withdraw: $"))
        if amount > balance:
            print("Insufficient funds!")
        else:
            balance -= amount
            save_balance(balance)
            print(f"Withdrew ${amount}. New balance: ${balance}")

    elif choice == "3":
        print("Thanks for banking with us. Goodbye!")
        break

    else:
        print("Invalid option, try again.")