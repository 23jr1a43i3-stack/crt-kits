n=int(input())
for i in range(1,n+1):
  print("{:2d}".format(i),end=" ")
  if i%4==0:
    print()