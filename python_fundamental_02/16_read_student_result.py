#Read student marks and calculate the average 
with open("python_fundamental_02/q16.txt",'w') as f:
    student="""
name : ankit
roll no : 123
mark obtained:
maths : 99
english : 90
hindi : 92
social science : 95
science : 97
"""
    f.write(student)

with open("python_fundamental_02/q16.txt",'r') as f:
    data=f.read()

number=[]
for i in data.split():
    try:    
        number.append(int(i))
    except ValueError:
        pass
print(number)
def avg(number):
    num=0
    for i in range (1,len(number)):
        num+=number[i]

    return num/(len(number)-1)

print(f"avg of student mark = {avg(number)}")