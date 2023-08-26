# wap to pass a no. to  a function then  print 1 ,2,3,4,,5,,6,6,7.....n using recursion

def rec(n):
    if n==0:
        return 
    rec(n-1)
    print(n)


n=int(input("enter number :"))
rec(n)



