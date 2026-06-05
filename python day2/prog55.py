Str = "scott@oracle.in" # The input string
a = Str.find('@')      # Finds the index of '@' (index 5)
d = Str.find('.')      # Finds the index of the first '.' (index 12)

print(Str[0:a])        # Slices from start to '@'. Output: scott
print(Str[a+1:d])      # Slices from after '@' to '.'. Output: oracle