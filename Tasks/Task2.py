# Operators
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /, %, //, **): ")
if op == '+':
    res = a + b
elif op == '-':
    res = a - b
elif op == '*':
    res = a * b
elif op == '/':
    if b != 0:
        res = a / b
    else:
        res = "Error: Division by zero"
elif op == '**':
    res = a ** b
elif op == '//':
    res = a // b
else:
    res = "invalid operator..."

print(f"{a} {op} {b} = {res}")

