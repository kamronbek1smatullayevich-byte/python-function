def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    if amount > balance:
        print("Balans yetarli emas")
        return balance
    return balance - amount

def check_balance(balance):
    print("Balansingiz:", balance)


balance = 100000

operation = input("Amalni tanlang: deposit, withdraw, check: ")

if operation == "deposit":
    amount = float(input("Pul kiriting: "))
    balance = deposit(balance, amount)
    check_balance(balance)

elif operation == "withdraw":
    amount = float(input("Yechmoqchi bo‘lgan pulni kiriting: "))
    balance = withdraw(balance, amount)
    check_balance(balance)

elif operation == "check":
    check_balance(balance)

else:
    print("Noto‘g‘ri amal")