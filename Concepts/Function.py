# Fn with print
def display():  
    print("Hai, this is Python")

display()

# Fn with return
def add(a,b):
    return a+b

result = add(5,5)
print(result)

# Local var
def show():
    msg = "Python"
    print(msg)

show()

# Global var
msg = "Python Programming!"
def display():
    print("Inside function:", msg)

display()
print("Outside function:", msg)

# Recursion 
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))

# Lambda fn
square = lambda n: n * n
print(square(7)) 

# Using  lambda with filter()
n = [1, 2, 3, 4, 5, 6,7]
odd = filter(lambda x: x % 2 != 0, n)
print(list(odd))

# Using  lambda with map()
a = [1, 2, 3, 4]
b = map(lambda x: x * 2, a)
print(list(b))

# Using lambda with reduce()
from functools import reduce
a = [1, 2, 3, 4]
b = reduce(lambda x, y: x * y, a)
print(b)

#  *args and **kwargs
def profile(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)
profile("Aishu", "Python", age=17, city="Namakkal")
