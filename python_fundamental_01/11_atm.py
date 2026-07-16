"""
Simple ATM Menu
Create a menu:
1 → Check Balance
2 → Deposit
3 → Withdraw
4 → Exit
Use variables for the balance and handle invalid choices.
"""
def menu(choice,balance):
    if choice == 1:
        print(f"your balance is {balance}")
    elif choice == 2:
        deposite=float(input("money to deposited "))
        if deposite>0:
            balance+=deposite
            print("money deposite successfully")
    elif choice == 3:
        withdraw=float(input("enter the value"))
        if balance>=withdraw:
            balance-=withdraw
            print("print withdraw successfully")
        else:
            print("insufficient balance")
    elif choice==4:
        print("exit")
    else:
        print("invalid choice")
    return balance

print("deposite your money \n")
balance=float(input("enter your balance"))
while True:
    print("menu")
    print("enter 1 for check balance")
    print("enter 2 for deposite")
    print("enter 3 for withdraw")
    print("enter 4 for exit")
    choice=int(input("enter your choice"))
    balance=menu(choice,balance)
    if choice ==4:
        break