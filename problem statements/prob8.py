log=list(map(int,input('Enter the logs : ').split()))
last_5=log[-5:]
print(f"last 5 : {last_5} | Critical error Found: {True if 500 in last_5 else False}")