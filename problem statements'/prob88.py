n = int(input())

for i in range(n, 0, -1):
    print("  " * (n - i), end="")
    for j in range(i):
        print(chr(96 + i), end=" ")
    print()