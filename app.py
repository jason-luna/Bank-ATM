from banking_pkg import account


def atm_menu(name):
    print("")
    print("     === Automated Teller Machine ===     ")
    print("               User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


# ----register a new user----
print("          === Automated Teller Machine ===          ")
# register name
while True:
    name = input("Enter name to register: ")
    if len(name) >= 1 and len(name) <= 10:
        name = name
        break
    else:
        print("The maximum name length is 10 characters")
# register PIN
while True:
    pin = input("Enter PIN: ")
    if len(pin) == 4 and pin.isnumeric() == True:
        pin = pin
        break
    else:
        print("PIN must contain 4 numbers")
balance = 0.0
print(f'{name} has been registered with a starting balance of ${balance}')

# ----user login----
while True:
    print("          === Automated Teller Machine ===          ")
    print("LOGIN")
    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")
    if name_to_validate == name and pin_to_validate == pin:
        print("Login successful!")
        break
    else:
        print("Invalid credentials")

# ----atm menu options----
while True:
    atm_menu(name)
    option = input("Choose an option: ")
    if option == "1":
        account.show_balance(balance)
    elif option == "2":
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif option == "3":
        new_balance = account.withdraw(balance)
        if new_balance < 0.0:
            print("Get your money up not your funny up!")
            account.show_balance(balance)
        elif new_balance >= 0.0:
            balance = new_balance
            account.show_balance(balance)
    elif option == "4":
        account.logout(name)
        break
    else:
        print("Invalid option!")
