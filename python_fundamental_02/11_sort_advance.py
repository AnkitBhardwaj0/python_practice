#Lambda to sort tuples by age.
#If two people have the same age, sort them by name (alphabetically)
boy=[
    ("Ankit", 21),
    ("Rahul", 19),
    ("Amit", 23),
    ("Shan", 20),
    ("Abhishek",19)
]

print(sorted(boy,key=lambda x:(x[1],x[0])))