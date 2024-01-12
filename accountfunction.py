minimum_balance=20000


def deposit():
    deposit_value=int(input("enter your deposit:"))
    amount=minimum_balance+deposit_value
    print("The amount you deposited is",deposit_value) 
    print("The minimum amount is: ",minimum_balance)
    print("your total balance is",amount)
    
def withdraw():
    withdraw_amount=int(input("enter your withdraw amount:"))
    amount=minimum_balance-withdraw_amount
    print("your withdraw amount is : ",withdraw_amount)
    print("minimum value is:",minimum_balance)
    print("your account balance is :",amount)
def balance():
    print("your balance is :",minimum_balance)









account_number=int(input("enter your account no:"))
print("1.deposit\n 2.withdraw \n 3.balance 4.exit")
check=int(input("enter your choice:  "))
if check==1:
    deposit()
elif check==2:
    withdraw()
elif check==3:
    balance()

    
        
        


