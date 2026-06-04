num=int(input("Enter a number"))
for i in range(1,num+1):
    print(f"Muntiplication table of{i}:")
    print("----------------------------")
    for j in range(1,11):
        print(f"{i}x{j}={num*i}")