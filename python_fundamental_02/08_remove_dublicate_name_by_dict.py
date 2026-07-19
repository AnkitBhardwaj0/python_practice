#Remove duplicate names while keeping order.(using dict)
names=["ankit","shan","amit","ankit","amit","shan","saurav","dev","saurav","dev"]
remove_duplicate_names={}
for name in names:
    remove_duplicate_names[name]=1
print(remove_duplicate_names.keys())