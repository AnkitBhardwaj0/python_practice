"""
Student Grade System
Take marks in 5 subjects.
Print:
Total
Percentage
Grade (A, B, C, D,E, F)"""
def total(marks):
    return sum(marks)

def percentage(marks):
    percent=total(marks)/len(marks)
    return percent

def grade(marks):
    percent= percentage(marks)
    if 100 >= percent > 90:
        return 'A'
    elif 90 >= percent > 80:
        return 'B'
    elif 80 >= percent > 60:
        return 'C' 
    elif 60 >= percent > 40:
        return 'D'
    elif 40 >= percent > 30:
        return 'E'
    else:
        return 'F'

def show_result(marks):
    print(f"total marks ={total (marks)}")
    print(f"percentage = {percentage(marks)} %")
    print(f"{grade(marks)}  grade")

def all_sub_marks():
    marks=[]
    for i in range(5):
        mark=(float(input(f"enter mark of subject {i+1} ")))
        while (mark>100) or (mark<0):
            print("plz enter valid number")
            mark=(float(input(f"enter mark of subject {i+1} "))) 
        marks.append(mark)           
    return marks

show_result(all_sub_marks())
