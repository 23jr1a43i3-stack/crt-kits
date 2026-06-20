n=int(input('Enter the value :'))
k=1
for i in range(1,n+1):
  
  ch = chr(64 + i)
  for j in range(1,n+1):
    print(ch,end="")
  print()