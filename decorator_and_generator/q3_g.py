def fibonacci(num):
    a,b=0,1
    for i in range(num):
        yield a
        a,b=b,a+b
       
def square(num):
        for i in num:
            yield i*i

print(sum(square(fibonacci(10))))
for value in square(fibonacci(10)):
    print(value)

