#Read student marks and calculate the average
with open("python_fundamental_02/q15.txt",'w') as f:
    student="""
name : ankit
mark obtained:
maths : 99
english : 90
hindi : 92
social science : 95
science : 97
"""
    f.write(student)

with open("python_fundamental_02/q15.txt",'r') as f:
    data=f.read()

number=[]
for i in data.split():
    try:    
        number.append(int(i))
    except ValueError:
        pass

def avg(number):
    num=0
    for i in number:
        num+=i
    return num/len(number)

print(f"avg of student mark = {avg(number)}")