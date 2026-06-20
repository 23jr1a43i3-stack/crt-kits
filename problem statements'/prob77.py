n = int(input())

for i in range(n):
    print(chr(64 + n - i) * (i + 1))