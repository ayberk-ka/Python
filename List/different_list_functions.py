#Methods Provided by Lists in Python

cood = ['programming', 'python']
cood2 = ['java', 'c++']

cood += cood2  # or cood.extend(cood2)
print('cood += cood2 = ' ,cood)

# Adds a new item to the end of a list
cood.append('html')
print("cood.append('html')= ", cood)

# Inserts an item at the ith position in a list
cood.insert(1, 'c#')
print("cood.insert(1, 'c#')= ", cood)

# Removes
cood.remove('programming')
print("cood.remove('programming')= ", cood)

# Deletes the item in the ith position
del cood[0]
print('del cood[0]= ', cood)

# Removes the last item in a list
cood.pop()
print('cood.pop()= ', cood)
print('cood.pop(1) = Removes and returns the ith item in a list: ',cood.pop(1))

# Returns the number of occurrences of item
print("cood.count('c++')= ",cood.count('c++'))

# Modifies a list to be sorted
cood.sort()
print('cood.sort= ', cood)

# Copy list to the new list
new_cood = cood.copy()
print('new_cood = cood.copy() =',new_cood)

# Removes all items from the list
cood.clear()
print('cood.clear()= ', cood)