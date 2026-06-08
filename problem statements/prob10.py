score=list(map(len,input('values:').split()))
print(f'average npd score : {sum(score)/len(score)}|nps score is : {True if sum (score)>=9 else False}')