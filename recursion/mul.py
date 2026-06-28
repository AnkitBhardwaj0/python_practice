#multiplication using recursion
def multiply(x,y):
    if y==0:
        return 0
    elif y==1:
        return x
    else:
        return x+multiply(x,y-1)
print(multiply(5,3))