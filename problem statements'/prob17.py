a=int(input())
b=int(input())
for i in range(a):
    for j in range(b):
        if i % 2 == 0:
            char = chr(65 + i)
            print(f"{char} ", end="")
        else:
            print("* ", end="")
print()