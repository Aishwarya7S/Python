#if
num = 7
if num > 5: 
    print("umber is greater than 5")

#if-else
age = 17
if age >= 18:
    print("Eligible to Vote")
else:
    print("Not eligible")

#if-elif-else
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: D")

#nested if
num = int(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")

#match-case or switch-case
number = 2
match number:
    case 1:
        print("One")
    case 2:
        print("Two")
    case _:
        print("Invalid")

