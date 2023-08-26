# 5. wap in pyhton to initialize a 3 digit integer and perform the addition of 1st digit and last digit of this no.
#       (using only operator)

a=int(input("enter a 3 digit no "))

print("displaying the reverse of it")
print("-----------------------------")
first=a%10
a=a//10
second=a%10
a=a//10
sum =first+a
print(f"first digit ={a}")
print(f"last digit ={first}")

print(f"sum  = {sum}")