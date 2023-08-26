# WAP TO CHECK A ENETERED VALUE IS PRESENT IN THE SET OR NOT

set1={1,2,3,4,5,6}

n=int(input("enter a no. to check if it is present or not"))


# for i in set1:
#     if i is n:
#         print(f"{n} is present in the list")
#         break
# else:
#     print(f"{n} is not present")

if n in set1:
        print(f"{n} is present in the list")
else:
         print(f"{n} is not present")