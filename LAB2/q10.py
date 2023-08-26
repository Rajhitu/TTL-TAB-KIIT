# wap to print following pattern
# 1
# 2 3
# 4 5 6
# 7 8 9 10
x=1
for i in range(1, 5):
 
 print(" ")
 for j in range(1, i+1):
        print(f"{x} ", end="")
        x+=1
 