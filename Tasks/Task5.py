# Functions
def fact(n):
    fact =1
    for i in range(1, n + 1):
        fact *= i
    return fact

num = int(input("Enter a number: "))
print("Output →", fact(num))

print("Add function with *args")
def add(*args):
    return sum(args)

result = add(1,2,3,4,5)
print("Output :" , result)