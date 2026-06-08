price=list(map(int,input("Enter the price of 5 items :").split()))
print([i for i in price if i>1000])