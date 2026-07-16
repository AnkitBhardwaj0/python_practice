#Print the sum of numbers from 1 to n.
def sum(n):
    add=0
    for i in range(1,n+1):
        add+=i
    print(f"sum of n natural number is {add}")

sum(5)
sum(10)