"""
Employee Salary Calculator
Take as input:
Employee name
Basic salary

Calculate:

HRA = 20% of basic salary
DA = 10% of basic salary
Tax = 5% of gross salary (Basic + HRA + DA)

Print:
Gross Salary
Tax
Net Salary
"""
def hra(salary):
    return salary*20/100

def da(salary):
    return salary*10/100

def gross_salary_calculator(salary):
    return salary+hra(salary)+da(salary)


def tax_count(gross):
    return gross*5/100

def net_salary(gross,tax_amount):
    return gross-tax_amount

def show(name,gross,salary,tax_amount):
    print(f"name of employee {name}")
    print(f"gross salary = {gross}")
    print(f"hra = {hra(salary)}")
    print(f"da = {da(salary)}")
    print(f"net slaray = {net_salary(gross,tax_amount)}")
    print(f"tax = {tax_amount}")

while True:
    name=input("enter name of employee :")
    while True:
        salary=float(input("salary of empoloyee :"))
        if salary>0:
            break
        else:
            print("enter valid salary")
    gross=gross_salary_calculator(salary)
    tax_amount=tax_count(gross)
    show(name,gross,salary,tax_amount)
    
    print(" if you want use next time say yes")
    need=input("enter your need")
    if need != "yes":
        break

        
    