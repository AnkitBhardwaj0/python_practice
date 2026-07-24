def my_range(start,end):
    for i in range (start,end):
        yield i


gen=my_range(1,5)
for i in gen:
    print(i)