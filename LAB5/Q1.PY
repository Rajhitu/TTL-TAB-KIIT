# Q1.WAP TO CHECK 2 GIVEN SETS HAVE COMMON ELEMENT OR NOT

set1={1,2,3,4,5}

set2={6,7}
c=0
for i in set1:
    if(i in set2):
        c+=1


if c == 0:
    print(" the sets has no common elements")
else:
     print("Both the sets has  common elements")