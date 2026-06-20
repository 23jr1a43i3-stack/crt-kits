n=int(input('Enter the value :'))
for i in range(n,0,-1):
  ch = chr(64 + i)
  for j in range(1,n+1):
    print(ch,end="")
  print()