n = int(input())
for i in range(1, n + 1):
    k = 0  
    for j in range(1, (n - j + 2)):
        print((n - k)*(n-k), end=" ")
        k += 1
    print()