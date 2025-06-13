name = input("Enter your name: ")
print("Hello", name)

age = int(input("Enter your age: "))
print("Your Age is :", age)

value = float(input("Enter your marks: "))
print("Marks -", value)

x, y = input("Enter two input: ").split()
print("x:", x, "y:", y)

a, b = map(int, input("Enter two numbers: ").split())
print("Product:", a * b)

#Output Formatting
amount = 130.75
print("Amount : ${:.2f}".format(amount))        #Using Format()
print(f"Hello {name} and your age is {age}!")   #Using f-string
print("Python", end= '@')                       #Using sep and end parameter
print("Programming")
print('01', '01', '2017', sep='-')
sum = age+5 
print( "The sum is %d" %sum)                    #Using % Operator