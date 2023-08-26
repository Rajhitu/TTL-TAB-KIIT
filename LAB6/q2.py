# wap in python to pass a list to a function, now function adds 3 to each and 
#  every element of the list and print the updated list inside the function calll

def list_upd(a):
    for i in range(len(a)):
        a[i]+=3
        # print(i)
    print(a)


a=[1,2,3,4,5]
list_upd(a)
print(a)

