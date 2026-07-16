"""
Banking System (Without OOP)

Create a menu-driven program with these options:

Create Account
Deposit Money
Withdraw Money
Check Balance
Exit

Rules:

Balance cannot become negative.
Deposit amount must be positive.
Withdrawal amount must be positive.
Show appropriate messages for invalid operations.
"""
def create_account(member):
    acc_num=len(member)+1
    name=input("enter your name : ")
    balance=0
    member[acc_num]={
        "name":name,
        "acc_number":acc_num,
        "balance":balance
    }
    print(f"name = {member[acc_num]['name']} \naccount number = {member[acc_num]['acc_number']}")

def deposite_money(member):
    bank_id=int(input("enter your bank account number"))
    if bank_id in member:
        money=(float(input("enter money to deposited : ")))
        if money>0:
            member[bank_id]["balance"]+=money
            print("money deposited sucessfully !")

        else:
            print("sorry ! invalid money")
    else:
        print("invalid account user")

def withdraw_money(member):
    bank_id=int(input("enter your bank account number"))
    if bank_id in member:
        money=(float(input("enter money")))
        if member[bank_id]["balance"] >= money > 0:
            member[bank_id]["balance"]-=money
            print("monet withdraw successfully !")
        else:
            if money <= 0:
                print("Amount must be positive.")
            elif money > member[bank_id]["balance"]:
                print("Insufficient balance.")
    else:
        print("invalid account user")
        
def check_balance(member):
    bank_id=int(input("enter your bank account number"))
    if bank_id in member:
        print(f"available balance = {member[bank_id]['balance']}")
    else:
        print("invalid account user")
    
def exit_program():
    print("thank you for visiting")  

member={}
while True:
    print("welcome to an bank")
    print("how may i help you ! ")
    print("click 1 for create account :")
    print("click 2 for deposite money :")
    print("click 3 for withdraw money :")
    print("click 4 for check balance :")
    print("click 5 for exit the program :")
    choice=int(input("enter your choice : "))
    if choice==1:
        create_account(member)
    elif choice==2:
        deposite_money(member)
    elif choice==3:
        withdraw_money(member)
    elif choice==4:
        check_balance(member)
    elif choice==5:
        exit_program()
        break
    else:
        print("invalid choice")
