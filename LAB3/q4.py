# wap in pyhtin to check given string is plaondrome string or not

n=input("enter a string ")

rev=""

# finding the length
count=0
for i in n:
   count+=1

while count:
   rev+=n[count-1]
   count-=1

if(rev==n):
    print("yes it is a palindrome no.")
else:
    print("no it is a palindrome no.")
