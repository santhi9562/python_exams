month=int(input("enter your choice:"))

if month==1:
    print("month is january and 31 days")
elif month==2:
    year=int(input("enter your year:"))

    if year%4==0:
        print("month is february and 29 days")
    else:
        print(" your month is february and 28 days")
elif  month==3:
    print("month is march and 31 days")
elif month==4:
    print("month is april and 30 days")
elif month==5:
    print("month is may and 31 days")
elif month==6:
    print("month is june and 30 days")
elif month==7:
    print("month is july and 31 days")
if month==8:
    print("month is august and 31 days")
if month==9:
    print("month is september and 30 days")
elif month==10:
    print("month is october and 31 days")
elif month==11:
    print("month is november and 30 days")
elif month==12:
    print("month is december and 31 days")
else:
    ("invalid")