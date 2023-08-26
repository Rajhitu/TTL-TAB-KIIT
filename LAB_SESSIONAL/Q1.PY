def check_prime(n):
    for i in range(2,n):
        if(n%i==0):
            return False
    return True
        
n=int(input("enter a no"))
c=0
for i in range(2,(n//2)+1):  
 if check_prime(i): 
    if check_prime(n-i):
        print(f"yes {i}+{n-i}")
        c+=1
        

if c==0:
    print("cant be expressed as a sum")