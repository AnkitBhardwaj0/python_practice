#Take three numbers and print the largest one.
def largest_no(num1,num2,num3):
    if num1>=num2 and num2>=num3:
        print(f"{num1} is largest ")
    if num1==num2==num3:
        print("all are equal ")
    elif num2>=num3:
        print(f"{num2} is largest")
    else:
        print(f"{num3} is largest")

largest_no(1,1,1)
largest_no(1,2,2)
largest_no(2,3,4)
largest_no(1,0,1)
largest_no(1,1,2)
largest_no(2,2,1)