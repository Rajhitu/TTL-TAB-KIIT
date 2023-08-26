# wap in python to input a string and display reverse of it

s=input("enter a string ")

# finding the length
count=0
for i in s:
   count+=1

while count:
    print(s[count-1],end="")
    count-=1

# print("length of the string is "+str(count))
