# wap in python to enter a 3 digit no. from keyboard and check whether it is palindrome no or not
# without using any Loop 

a= int(input("enter a 3 dig no"))
temp=a
# b=0
# while a>0:
#   b=(b*10)+(a%10)
#   a=a//10
rev=0
rev=(rev*10)+temp%10
temp//=10
rev=(rev*10)+temp%10
temp//=10
rev=(rev*10)+temp%10


if rev==a:
 print(f"{a} is palindrome no")
else:
  print(f"{a} is not palindrome no")