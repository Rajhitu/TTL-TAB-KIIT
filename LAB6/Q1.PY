#WAP TO CALCULATE Si of the given ptr using function where the function takes the default value for the r

def si_cal(p,t,r=5):
    ans= (p*r*t)/100
    return ans

p=int(input("enter principle :"))
r=int(input("enter rate :"))
t=int(input("enter time :"))
print(f"the si is-->{si_cal(p,t,r)}")