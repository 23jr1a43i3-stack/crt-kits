n = int(input())

for i in range(n, 0, -1):
    k=1
    print("  " * (n - i), end="")
    for j in range(i):
        print(chr(97 + j), end=" ")
        k+=1
    print()