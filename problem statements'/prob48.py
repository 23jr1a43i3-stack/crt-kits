n=int(input('Enter the integer :'))
k = 1
for i in range(1, n+1):
    for j in range(1, n+1):
      print("{:2d}".format(k*k),end=" ")
    k+=2
    print()