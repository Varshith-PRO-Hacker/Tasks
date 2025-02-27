def logged(func):
     def wrapper(*args, **kwargs):
          print(f"Function {func.__name__}: {func(*args, **kwargs)}")
          return func()
     return wrapper

@logged
def print_all(*args, **kwargs):
     # *args = allows you to take unlimited number of positional arguments
     # **kwargs = allows you to take unlimited number of keyword arguments.
    return f"Positional: {args}, Keywords: {kwargs}"

@logged
def add(*args, **kwargs):
     return (f"returned: {sum(args) + sum(kwargs.values())}")

print_all(1, 2, 3, height=6.3, age=16)
add(1, 2, 3, height=6.3, age=16)