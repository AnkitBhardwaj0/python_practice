# Even Numbers
it=iter(range(1,11))
while True:
    try:
        num=next(it)
        if num%2==0:
            print(num)
    except StopIteration:
        break