# wap in pyhton to input 3 stings and try to delete 1 of the string 
# also check the types of the string ans adreres of the string

first=input("enter the first string :")
second=input("enter the second string :")
third=input("enter the third string :")

# print("deleting 1st sttring")
# first=""



print("types of the strings  are :")
print(f"{type(first)}\t{type(second)}\t{type(third)}\n\n")

print("address of the strings  are :")
print(f"{id(first)}\t{id(second)}\t{id(third)}")



print("deleting 1st sttring")
del(first)

print("after deleting the string becoomes:")
print(f"\t{second}\t{third}")