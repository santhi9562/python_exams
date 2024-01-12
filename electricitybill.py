a=int(input("enter your unit:"))
if a<=100:
    c=a*0
    print("you have no charge:",c)
elif a>=100 and a<200:
    c=a*0+a*5
    print("your bill is",c)
elif a>=200:
    c=a*0+a*5-a*10
    print("your bill is",c)