# List
lists = ['orange', 'skyblue', 'green', 'red','black']
print("List items:")
for item in lists:
    print(item, end=' ')
print()

listn = [1,2,3,6,7,8,10]
print("Even numbers in list:")
for item in listn:
    if(item % 2 == 0):
        print(item , end =' ')
    else:
        continue
