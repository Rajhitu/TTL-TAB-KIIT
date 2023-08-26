# abc

#abc,bac,cab

def swap(str,i):
    t=str[0]


str=input("enter a  string")
for i in range(0,len(str)):
    temp=list(str)
    t=temp[0]
    temp[0]=temp[i]
    temp[i]=t
    ans=""
    for i in range(0,len(temp)):
        ans=ans+temp[i]
    
    print(ans)

