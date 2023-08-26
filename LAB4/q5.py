# wap to change the position of enery nth element with n+1 element

list=[1,2,3,4,5,6,7,8]

print(f"BEFORE:{list}")
for i in range(0,len(list)-1):
    list[i]=list[i+1]

print(f"AFTER:{list}")
