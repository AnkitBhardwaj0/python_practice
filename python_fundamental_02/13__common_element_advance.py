#Find common elements between two files.
with open("python_fundamental_02/q2.txt",'r') as f:
    data1=set(f.read().split())
with open("python_fundamental_02/q12.txt",'r') as f:
    data2=set(f.read().split())

print("common elements between two files")
print(data1 & data2)