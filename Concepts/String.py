s = "  Python course  "

print("Original:", s)
print("Length:", len(s))
print("Upper:", s.upper())
print("Lower:", s.lower())
print("Swapcase:", s.swapcase())
print("Capitalize:", s.capitalize())
print("Title:", s.title())
print("Starts with 'Py':", s.startswith("Py"))
print("Ends with 'course':", s.endswith("course"))
print("Count of 'o':", s.count("o"))
print("Find 'c':", s.find("c"))
print("Index of 't':", s.index("t"))
print("Replace 'course' with 'tutorial':", s.replace("course", "tutorial"))
print("Strip:", s.strip()) 
print("Split:", s.split())
print("Join with '-':", "-".join(s.split()))
print("Is alpha:", s.isalpha())
print("Is digit:", s.isdigit())
print("Is space:", s.isspace())
print("Is alnum:", s.isalnum())
