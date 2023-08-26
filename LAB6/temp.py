mylist=["madhu","bibhu","dikhu"]


length=len(mylist[0])
ans=0
for i in range(0,length):
    temp=mylist[0][0+i]
    print(f"temp-->{temp}")
    print("----------------------")
    check=0
    for j in mylist:
        print(f"j[i]--------->{j[i]}")
        if j[i]==temp:
            check+=1
            
    if check==len(mylist):
        ans+=1

print(ans)