import os

filename = "student.txt"

# Write
with open(filename, 'w') as file:
    file.write("Hai, this is python \n")
    file.write("File handling concept \n")
print("File written successfully.\n")

# Read
with open(filename, 'r') as file:
    content = file.read()
    print("File content:\n",content)

# Append
with  open(filename, 'a') as file:
    file.write("This will add an extra line")
print("Data appended successfully.\n")

print("Reading line-by-line: \n")
with open(filename, "r") as file:
    for line in file:
        print(line.strip())

# Check if file exists & delete
if os.path.exists(filename):
    print("\nFile exists. Ready to delete.")
    os.remove(filename)
    print("File deleted successfully.")
else:
    print("File not found.")





