a = 10
b = 3

print("Arithmetic Operators:")
print("Addition:", a + b)       #13
print("Subtraction:", a - b)    #7
print("Multiplication:", a * b) #30
print("Division:", a / b)            #3.3333333
print("Floor Division:", a // b)     #3
print("Modulus:", a % b)    #1
print("Exponent:", a ** b)  #1000
print("\n")

print("Comparison Operators:")
print("a == b:", a == b)    #F
print("a != b:", a != b)    #T
print("a > b:", a > b)      #T
print("a < b:", a < b)      #F
print("a >= b:", a >= b)    #T
print("a <= b:", a <= b)    #F
print("\n")

x = 5
print("Assignment Operators:")
x += 2
print("x += 2:", x)   #7
x -= 1
print("x -= 1:", x)   #6
x *= 3
print("x *= 3:", x)   #18
x /= 2
print("x /= 2:", x)   #9.0
x %= 3
print("x %= 3:", x)   #0.0
x **= 2
print("x **= 2:", x)  #0.0
x //= 2
print("x //= 2:", x)  #0.0
print("\n")

p = True
q = False
print("Logical Operators:")
print("p and q:", p and q)  #F
print("p or q:", p or q)    #T
print("not p:", not p)      #F
print("\n")

m = 6       # 110
n = 3       # 011
print("Bitwise Operators:")
print("AND:", m & n)      # 010 -> 2
print("OR:", m | n)       # 111 -> 7
print("XOR:", m ^ n)      # 101 -> 5
print("NOT (~m):", ~m)    # -(m+1) -> -7
print("Left Shift:", m << 1)    # 1100 -> 12
print("Right Shift:", m >> 1)   # 011 -> 3
print("\n")

print("Identity Operators:")
print("m is n:", m is n)            #F
print("m is not n:", m is not n)    #T
print("\n")

my_list = [1, 2, 3, 4, 5]
print("Membership Operators:")
print("3 in my_list:", 3 in my_list)            #T
print("2 not in my_list:", 2 not in my_list)    #F

print("Ternary Operator:")
num = 7
result = "Even" if num % 2 == 0 else "Odd"
print(result)  #odd
