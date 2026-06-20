n = int(input())

for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    for j in range(i):
        print(chr(64 + n - j), end=" ")
    print()