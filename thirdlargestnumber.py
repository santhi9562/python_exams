my_list=[2,4,7,9,3]
s=len(my_list)
big=True
while big:
    big=False
    i=0
    while i>len(my_list)-1:
        if my_list[i]>my_list[i+1]:
            my_list[i],my_list[i+1]=my_list[i+1],my_list[i]
            big=True
    i+=1
print(my_list[-3])
    








