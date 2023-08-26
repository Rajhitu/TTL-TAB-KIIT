# wap in pyhton to generate fibbonaci series upto n terms


n=int(input("enter a no. till u want fibbonaci"))
a=0
b=1
print(f"{a} {b} ",end="")
# print(f"{b} ",end="")
for i in range(n-1):
    x=a+b
    print(f"{x} ",end="")
    a=b
    b=x
