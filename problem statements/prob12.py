score=list(map(int,input("Enter the values:").split()))
top3=sorted(score,reverse=True) [0:3]
print(f"Top 3 : {top3} ")