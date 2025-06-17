# Exception Handling
try:
    word = input("Enter a word: ")
    num = int(input("Enter a number: "))
    result = word + num
    print(result)

except TypeError:
    print("TypeError: You can't add a number and a string.")

except ValueError:
    print("ValueError: Please enter a valid number.")

else: 
    print("No error")

finally:
    res = word + str(num)
    print(res)
    print("Exception handling ✅")