# Tuple
tup1 = ("success", "work", "dream", "quote")
tup1 = tup1 + ("journey",)
print(tup1)
tup2 = ("hobby", "enjoy")
tup = tup1+tup2
print(tup)
print("Index of dream:", tup1.index("dream"))
print("Length:", len(tup2))

me = ("Aishu", 20, 'A')
name, age, grade = me
print("Name:", name)
print("Age:", age)
print("Grade:", grade)

num = (1,3,7)
print("Sum:", sum(num))
print("Max num:",max(num) )
print("Min num:", min(num))