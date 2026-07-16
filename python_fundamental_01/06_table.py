#Take a number and print its multiplication table up to 10.
def table(num):
    print(f"table of {num}\n")
    for i in range(1,11):
        print(num ," x ", i," = ",num*i)
    print(" ")

table(5)
table(6)
        
