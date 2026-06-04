a = [1,2,35,6,8,6,5,8,99,0,66]

print("Original List:", a)

# append(5)
a.append(5)
print("After append(5):", a)

# insert(2,85)
a.insert(2, 85)
print("After insert(2,85):", a)

# remove(2)
a.remove(2)
print("After remove(2):", a)

# pop()
a.pop()
print("After pop():", a)

# pop(index_of_0)
index_0 = a.index(0)
a.pop(index_0)
print("After pop(index_of_0):", a)

# index(85)
print("Index of 85:", a.index(85))

# count(2)
print("Count of 2:", a.count(2))

# sort()
a.sort()
print("After sort():", a)

# reverse()
a.reverse()
print("After reverse():", a)

# slicing
print("First 5 elements:", a[:5])
print("Last 5 elements:", a[-5:])
print("Elements from index 2 to 6:", a[2:7])

# append(sum(list))
a.append(sum(a))
print("After append(sum(list)):", a)

# append(max(list))
a.append(max(a))
print("After append(max(list)):", a)

# find length
print("Length of list:", len(a))

# find indexes of max and min
print("Index of max value:", a.index(max(a)))
print("Index of min value:", a.index(min(a)))

# index of 0 (if present)
if 0 in a:
    print("Index of 0:", a.index(0))
else:
    print("0 is not present in the list")