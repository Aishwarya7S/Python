# Conditional Statements
name = input("Enter your name: ")
marks = float(input("Enter your marks: "))

if marks >= 90:
    res = "A"
elif marks >= 80:
    res = "B"
elif marks >= 70:
    res = "C"
elif marks >= 50:
    res = "D"
else:
    res = "E - You need to improve"

print(f"Name:{name} and Grade: {res}")
