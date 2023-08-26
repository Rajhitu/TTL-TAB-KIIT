# write a pyhton program to remove all duplicates from a list

lists=[1,1,2,3,4,5,5,5,1,1,2]

# for i in list:
#     while list.count(i)!=1:
#         list.remove(i)

sets=set(lists)
lists=list(sets)

print(lists)