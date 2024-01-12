price=int(input("enter your prize:"))

if price>100000:
    print("your tax is:15%")
elif 50000<price<=100000:
    print("your tax is:10%")
else:
    print("your tax is :5%")