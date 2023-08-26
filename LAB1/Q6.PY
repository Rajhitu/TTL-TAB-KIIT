# 6. wap in pyhton to initialze a 3 digit no. and display reverse of it

a=int(input("enter a 3 digit no "))

print("displaying the reverse of it")
print("-----------------------------")
first=a%10
a=a//10
second=a%10
a=a//10
print(f"reverse ={first}{second}{a}")