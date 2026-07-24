def decorator(function):
    def wrapper(*args, **kwargs):
        print("Before")
        result = function(*args, **kwargs)
        print("After")
        return result
    return wrapper

@decorator
def greet(name):
    print(f"Hello {name}")

@decorator
def add(a, b):
    return a + b

greet("Ankit")
print(add(5, 7))