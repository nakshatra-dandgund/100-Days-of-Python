"""
Day 9 Project
ATM Machine Simulator
100 Days of Code – Python
Author: Nakshatra Dandgund
"""

balance = 50000
pin = 8619
attempts = 0

# PIN Verification (Max 3 attempts)
while attempts < 3:
    enter_pin = int(input("Enter your PIN: "))

    if enter_pin == pin:
        print("\nLogin Successful!")
        break
    else:
        attempts += 1
        print("Incorrect PIN")

# If all attempts are used
if attempts == 3:
    print("Too many incorrect attempts. Card blocked.")
else:
    # ATM Menu
    while True:
        print("\n------ ATM MENU ------")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        action = int(input("Enter your choice: "))

        if action == 1:
            print("Your balance is:", balance)

        elif action == 2:
            amount = int(input("Enter amount to deposit: "))
            balance += amount
            print("Amount deposited successfully!")
            print("Updated balance:", balance)

        elif action == 3:
            amount = int(input("Enter amount to withdraw: "))
            
            if amount > balance:
                print("Insufficient balance!")
                continue  # skip rest and go back to menu
            
            balance -= amount
            print("Withdrawal successful!")
            print("Remaining balance:", balance)

        elif action == 4:
            print("Thank you for using ATM. Goodbye!")
            break  # exit the loop

        else:
            print("Invalid option! Please choose between 1–4.")
            continue
