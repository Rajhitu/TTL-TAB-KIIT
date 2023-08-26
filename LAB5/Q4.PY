# WAP THAT FINDS ALL PAIRS OF ELEMENT   IN  A LIST WOSE SUM IS EQUALS TO A GIVEN VALUE

list=(1,2,3,4,5,6)
ans={}
sum=int(input("enter a the sum value"))


for i in  list:
    for j in range(i,len(list)):
        if sum-i==j:
            ans[i]=j

print(ans)