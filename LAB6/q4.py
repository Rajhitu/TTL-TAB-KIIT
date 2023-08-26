# wap in pyhton to generate a multiplication table of any no. using lamda function

# syntax funcname=lambda arg:exprsn


mul=lambda no,a:print(a*no,end=" ")

no=int(input("enter a no"))

for i in range(1,11):
    mul(no,i) 