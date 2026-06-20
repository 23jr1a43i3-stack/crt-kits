n = int(input())

for i in range(4, n - 1):
    print(" " * (n), end="")
    for j in range(i):
        print(chr(64 + n -1), end=" ")
    print()