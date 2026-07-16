#Print the factorial of a number.
def factorial(num):
    fact=1
    if num==(0,1):
       print(f" factorial of {num} is {fact}")
    else:
        for i in range(2,num+1):
            fact*=i
        print(f" factorial of {num} is {fact}")
factorial(1)
factorial(0)
factorial(5)
          