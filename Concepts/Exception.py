# Exc 1
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("Result:", result)
finally:
    print("Execution completed.")

# Exc 2  
try:
    x = int("abc")  
except (ValueError, TypeError) as e:
    print("Error occurred:", e)

# Exc 3
def set(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age set to {age}")

try:
    set(-5)
except ValueError as e:
    print(e)
