# wap to convert a tuple of string values to integer value

tuple1="1","2","3","4"

print(tuple1)
list =[]
for i in range(0,len(tuple1)):
      list.append(int(tuple1[i]))

list=tuple(list)
print(list)