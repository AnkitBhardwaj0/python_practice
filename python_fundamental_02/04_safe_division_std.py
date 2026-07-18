"""
Safe division using try-except.
It doesn't stop after an invalid input.
It keeps asking the user for numbers until valid input is entered.
"""
#Safe division using try-except.
def input_num():
    l=[]
    for i in range(0,2):        
        while True:
            try:
                l.append(int(input("enter number")))
            except ValueError:
                print("exception found :")
                print ("plz enter valid input as intger")
                
            else:
                break
    num1,num2 = l[0],l[1]
    return num1,num2


try:
    num1,num2=input_num()
    quotient=num1/num2
    rem=num1%num2
    floor_quotient=num1//num2
    print(f"division result \nreminder = {rem}\nquotient = {quotient}\nstandard_quotient={floor_quotient}")
except ZeroDivisionError:
    print("exception found :")
else:
    print("divide sucessfully")
finally:
    print("this is excption handling program")