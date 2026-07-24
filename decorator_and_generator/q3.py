def decorator(function):
    def wrapper(*args, **kwargs):
        print("Before")
        result = function(*args, **kwargs)
        print(result)
        print("After")
    return wrapper

@decorator
def add(a, b):
    return a + b

add(5, 6)