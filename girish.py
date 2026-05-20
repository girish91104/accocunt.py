# 1. Account Creation Module

def create_account():
    name = input("Enter Account Holder Name: ")
    pin = input("Set Your 4-Digit PIN: ")
    
    print("Account Created Successfully")
    print("Welcome", name)

create_account()

# 2. Deposit System

balance = 1000

def deposit():
    global balance
    
    amount = float(input("Enter Deposit Amount: "))
    balance = balance + amount
    
    print("Amount Deposited Successfully")
    print("Current Balance =", balance)

deposit()

# 3. Withdrawal System

balance = 5000

def withdraw():
    global balance
    
    amount = float(input("Enter Withdrawal Amount: "))
    
    if amount <= balance:
        balance = balance - amount
        print("Withdrawal Successful")
        print("Remaining Balance =", balance)
    else:
        print("Insufficient Balance")

withdraw()

# 4. Balance Inquiry

balance = 3500

def check_balance():
    print("Your Current Balance is =", balance)

check_balance()

# 5. Transaction History

transactions = [
    "Deposited ₹1000",
    "Withdrawn ₹500",
    "Deposited ₹2000"
]

def transaction_history():
    print("Transaction History")
    
    for t in transactions:
        print(t)

transaction_history()

# 6. PIN-Based Authentication

original_pin = "1234"

def login():
    entered_pin = input("Enter Your PIN: ")
    
    if entered_pin == original_pin:
        print("Login Successful")
    else:
        print("Incorrect PIN")

login()

# 7. Mini Statement Generation

name = "John"
balance = 4500

transactions = [
    "Deposited ₹1000",
    "Withdrawn ₹500",
    "Deposited ₹2000"
]

def mini_statement():
    print("----- MINI STATEMENT -----")
    print("Account Holder :", name)
    print("Available Balance :", balance)
    
    print("\nRecent Transactions:")
    
    for t in transactions:
        print(t)

mini_statement()
