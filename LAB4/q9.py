# wap to find out the multiplication of all the elements present in the tuple


list=[1,2,3,4,5]
print(list)
for i in list:
    print(f"{i}:",end=" ")
    for j in range(1,11):
        print(j*i,end=" ")
    print("")
    