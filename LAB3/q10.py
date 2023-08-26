# wap to demonstrate the predfine string function


s=input("enter a srting")

print("the string is upper case -->"+str(s.isupper()))
print("the string is lower case only  -->"+str(s.islower()))
print("the string alphabet only  -->"+str(s.isalpha()))
print("the string has digit only  -->"+str(s.isdigit()))
print("stripping the sring -->"+str(s.strip()))
print("string starts with 'h' -->"+str(s.startswith('h')))
print("string ends with 'r' -->"+str(s.endswith('r')))