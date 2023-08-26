# wap to print all distinct values present in the dictrionary
ans=set()
mydic = {"A": 1,
         "B": 2,
         "C": 2,
         "D": 3,
         "E": 3, 
         }

for  i in mydic:
    ans.add(mydic[i])

print(ans)