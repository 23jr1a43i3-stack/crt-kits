std={
    101:'scott',102:'smith',103:'jones',104:'miller'
    }
print(std)
std[103]='xyz'
print(std)
del std[101]
del std[103]
print(std)
check=102 in std
print(check)
check=101 in std
print(check)