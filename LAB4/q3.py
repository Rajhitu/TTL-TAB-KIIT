# wap to find out the index of an element in a specified list

list=[1,2,3,4,55,6]

n=int(input("enter the element u want to find the index i n list"))
print(list.index(n))

if n in list:
    for i in range(0,len(list)):
        if list[i] is n:
            print(f"index of {n} is {i}")
            break
else:
    print("this element is not present in list")
 