# File Handling
with open("myfile.txt", 'w') as file:
    file.write("Aishu \n")
    print("✅")

with open("myfile.txt", 'a') as file:
    file.write("File Handling in Python")

with open("myfile.txt", 'r') as file:
    content = file.read()
    print(content)