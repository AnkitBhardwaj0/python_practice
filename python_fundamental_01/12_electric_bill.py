"""
Electricity Bill
Calculate the bill using slabs:
First 100 units → ₹5/unit
Next 100 units → ₹8/unit
Above 200 units → ₹10/unit
Print the total bill.
"""
def electric_bill(consume):
    bill=0
    if consume<=100:
        bill=consume*5
    elif consume <= 200:
        bill=100*5+(consume-100)*8     
    else:
        bill=100*(8+5)+(consume-200)*10
    return bill
print("electric bill")
consume=float(input("enter electric consumption"))
print(f"total amount = {electric_bill(consume)}")