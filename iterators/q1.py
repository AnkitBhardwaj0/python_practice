#Count from 1 to 1Create an iterator that returns:
it=range(1,11)
it=iter(it)
while True:
    try:
        print(next(it))
    except StopIteration:
        break
