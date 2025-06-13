#while
count = 0
while count < 5:
    print(count)
    count += 1

#for
n = 3
for i in range(0,n):
    print(i)

#break 
for i in range(5):
    if i == 3:
        break
    print("NumberB:",i) 

#continue
for i in range(5):
    if i == 2:
        continue
    print("NumberC:",i) 

#pass
for i in range(5):
    if i == 2:
        pass 
    print("NumberP:", i)
