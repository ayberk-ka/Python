list=[]
counter=0 

while counter<10:
    counter+=1
    list.append(counter)
print(list)

# Check if a Number is Even or Odd in the list
for index in range(len(list)):
    if list[index] % 2 == 0:
        print(list[index], ' Is an even number')
    else:
        print(list[index], ' Is an odd number') 