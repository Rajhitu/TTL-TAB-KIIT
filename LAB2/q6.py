# wap in pyton to check the given no. is perfect no. or not
# sum of all its factors = no. itself

a=int(input("enter a no"))
sum=0
for i in range(1,a): 
    if a%i == 0:
        sum+=i

if(sum==a):
    print(f"{a} is  a perfect no")
else:
    print(f"{a} not  a perfect no")

