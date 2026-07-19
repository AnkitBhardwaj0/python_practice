#Remove duplicate names while keeping order.
names=["ankit","shan","amit","ankit","amit","shan","saurav","dev","saurav","dev"]
remove_duplicate_names=set()
new_list=[]
for name in names:
    if name not in remove_duplicate_names:
        new_list.append(name)
    remove_duplicate_names.add(name)
    
print(new_list)