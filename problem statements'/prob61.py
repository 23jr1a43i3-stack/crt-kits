n = int(input())
for i in range(1, n + 2):
    for j in range(n - i * 1):
        print(i*i, end=" ")
    print()