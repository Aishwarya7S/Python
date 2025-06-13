student = {"name": "Aishu", "age": 17, "course": "Python", "marks": 93}

student["grade"] = "A"                          
student["marks"] = 97                           
student.update({"city": "Namakkal"})           
student.update({"course": "Java"})             
print(student)

removed = student.pop("age")                   
print("Removed:", removed)

last_removed = student.popitem()                
print("Popitem:", last_removed)

value = student.get("marks")                    
print("Marks:", value)

print("Is 'name' in student?", "name" in student)  

print("Keys:", student.keys())                  
print("Values:", student.values())               
print("Items:", student.items())                 

copy_dict = student.copy()                      
print("Copy:", copy_dict)

student.clear()                                
print("After clear:", student)
