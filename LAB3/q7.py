# wap in python to cehck whether a particular string is availabe within  a string or not also print the given string as it is

n=input("enter a string: ")
check=input("enter the string u want to check: ")

if(check in n):
    print(f"{check} is availbe in {n} ")
else:
    print(f"{check} is not availbe in {n} ")
  