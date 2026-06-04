pin=int(input("Enter the PIN: "))
acc_bal=0
if pin==1234:
   print("Welcome to the bank")
while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice=int(input("Enter your choice: "))
    print("\n")
    if choice==1:
        amount=int(input("Enter the amount to deposit: "))
        acc_bal+=amount
        print(f"Dear customer your accountxxxxxxx1234 is created with {amount}")
    elif choice==2:
        amount=int(input("Enter the amount to withdraw: "))
        if(amount<acc_bal):
            print("Dear customer your accountxxxxxxx1234 is debited with {amount}")
            acc_bal=acc_bal-amount
            
        else:
            print("Insufficient balance")
    elif choice==3:
        print(f"Dear customer your accountxxxxxxx1234 has balance {acc_bal}")
    else:
        print("Thank you for using the bank")
        break
else:
    print("insufficient balance")
    
