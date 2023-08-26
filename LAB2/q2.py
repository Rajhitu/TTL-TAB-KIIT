# wap to enter 5 integer from the keyboard and find out the samllest one

a=int(input("enter 1st number "))
b=int(input("enter 2nd number "))
c=int(input("enter 3rd number "))
d=int(input("enter 4th number "))
e=int(input("enter 5th number "))

if a>b and a>c and a>d and a>e:
    print(f"{a} is greatest no")
elif b>a and b>c and b>d and b>e:
    print(f"{b} is greatest no")
elif c>b and c>a and c>d and c>e:
    print(f"{c} is greatest no")
elif d>b and d>c and d>a and d>e:
    print(f"{d} is greatest no")
else:
    print(f"{e} is greatest no")