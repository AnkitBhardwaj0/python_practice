#palindrome using recursion
def palindrome(s):
    if len(s)<=1:
        return "string is palindrome"
    elif s[0]==s[-1]:
        return palindrome(s[1:-1])
    else:
        return "string is not palindrome"
print(palindrome("abcba"))
