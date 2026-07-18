#Read numbers from a file and find the largest.
with open("python_fundamental_02\q1.txt" ,'w') as f:
    f.write("11 12 13 a 15")
with open("python_fundamental_02\q1.txt",'r') as f:
    data=f.read().split()
    largest=0
    for number in data:
        try:
            if largest<int(number):
                largest=int(number)
            
        except ValueError:
            pass

    if largest !=0:
        print(f"{largest} is largest")


