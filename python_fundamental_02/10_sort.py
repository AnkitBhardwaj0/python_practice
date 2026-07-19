#Lambda to sort tuples by age.
boy=[
    ("Ankit", 21),
    ("Rahul", 19),
    ("Amit", 23),
    ("Shan", 20)
]

print(sorted(boy,key=lambda x:x[1]))
print(sorted(boy,key=lambda x:x[1],reverse=True))
