#Check whether a number is a palindrome.
def palindrome(num):
    rev_num=0
    given_num=num
    while num>0:
        rem=num%10
        rev_num=rev_num*10+rem
        num=num//10 
    if given_num==rev_num:
        print(f"{given_num} is a palindrome Number")
    else:
        print(f"{given_num} is  not a palindrome Number")    

palindrome(55)
palindrome(11112111)
palindrome(1234321)