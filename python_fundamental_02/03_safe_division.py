#Safe division using try-except.
try:
    num1=float(input("enter the number"))
    num2=float(input("enter the number"))
    quotient=num1/num2
    rem=num1%num2
    floor_quotient=num1//num2
    print(f"division result \nreminder = {rem}\nquotient = {quotient}\nstandard_quotient={floor_quotient}")
except Exception as e:
    print(f"exception found : {e}")
else:
    print("divide sucessfully")
finally:
    print("this is excption handling program")