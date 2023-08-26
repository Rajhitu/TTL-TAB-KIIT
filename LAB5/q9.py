# wap toi convert a dicrionary into a list of list

list=[]
mydic = {"A": 7,
         "B": 25,
         "C":77,
         "D": 13,
         "E": 6, 
         }

for i in mydic:
    temp=[]
    temp.append(i)
    temp.append(mydic[i])
    list.append(temp)

print(list)