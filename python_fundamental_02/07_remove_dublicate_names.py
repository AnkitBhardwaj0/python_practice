#Remove duplicate names while keeping order.
names=["ankit","shan","amit","ankit","amit","shan","saurav","dev","saurav","dev"]
remove_duplicate_names=[]
for name in names:
    if name not in remove_duplicate_names:
        remove_duplicate_names.append(name)
print("name without duplicate")
print(remove_duplicate_names)
