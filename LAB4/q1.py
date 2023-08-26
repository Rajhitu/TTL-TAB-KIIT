# wap to get the 2nd smallest and 2nd largest element in the list


list = [1, 1, 2, 2, 2, 2, 2,  4, 4, 5, 6, 6 ,7, 7, 5, 5, 5, 5, 54, 4, 4, 4, 4, 44, 44, 33, 3, 3, 3, 3]

print(list)
for i in list:
        while list.count(i) != 1:
         list.remove(i)

print(list)
list.remove(max(list))



list.remove(min(list))

# print(max,min)
# ansmin = min

# for i in list:
#     if i > max:
#         ansmax = max
#         max = i

# for i in list:
#     if i < min:
#         ansmin = min
#         min = i


print("2nd largest element is --->"+str(max(list)))
print("2nd smallest element is --->"+str(min(list)))


# ======================================================================

# removing duplicate element


# for i in list:
#     while list.count(i) != 1:
#         list.remove(i)

# print(list)
# # sorting the lsit

# list.sort()
# print("2nd largest element is --->"+str(list[len(list)-2]))
# print("2nd smallest element is --->"+str(list[1]))

