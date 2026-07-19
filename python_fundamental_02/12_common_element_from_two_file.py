#Find common elements between two files.
with open("python_fundamental_02/q2.txt",'r') as f:
    data1=f.read().split()
with open("python_fundamental_02/q12.txt",'r') as f:
    data2=f.read().split()

print("common elements between two files")
for i in data1:
    if i in data2:
        print(i,end=" ")