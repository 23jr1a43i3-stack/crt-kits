score=list(map(int,input("Enter the scores for 5 students :").split()))
print(f"Rank :{sorted(score,reverse=True)} | Top Score :{max(score)}")