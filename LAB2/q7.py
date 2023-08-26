# wap in python to check whether a n. is armstrong or not
# (sum of the square od gditi is no. itself)\

a=int(input("enter a no"))
back=a
temp=a
dig=0
while temp>0:
    temp=temp//10
    dig+=1

sum=0

while a>0:
    temp=a%10
    sum=sum+(temp**dig)
    a=a//10
    


if(back==sum):
  print(f"{back}is a armstrong no")
else:
  print(f"{back} is not aa armstrong no") 
