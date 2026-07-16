#Reverse a number without converting it to a string.
def reverse(num):
    rev_num=0
    while num>0:
        rem=num%10
        rev_num=rev_num*10+rem
        num=num//10   
    print(f"reverse no is {rev_num}")
reverse(111)
reverse(121)
reverse(123)