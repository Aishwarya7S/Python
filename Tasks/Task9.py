# Dictionary
student = {1:'Rishi', 2:'Atharvaa', 3:'Ani'}
print("Keys:", student.keys())                  
print("Values:", student.values())               
print("Items:", student.items()) 
student.update({4: 'Guna'})
print(student)

word = "Aishaa"
freq = {}

for char in word:
    freq[char] = freq.get(char, 0) + 1

print("Character Frequency →", freq)