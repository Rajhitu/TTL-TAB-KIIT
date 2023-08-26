# wap in python to enter to a amrks of the student in 4 subjects then calculate the  total markss and percentage 

# also assign the grade as per the followuing criteria

# if %>=90 ->O 
# if %>=80 ->A 
# if %>=70 ->B
# if %>=60 ->C 

a=int(input("enter marks of 1st subj "))
b=int(input("enter marks of 2nd subj "))
c=int(input("enter marks of 3rd subj "))
d=int(input("enter marks of 4th subj "))

sum=a+b+c+d
avg=sum/4
perc=(sum/400)*100

print(f"your total  marks is {sum}")
print(f"your average   {avg}%)
print(f"your percentage is {perc}")

if avg>=90:
    print("your grade is O")
elif avg>=80:
     print("your grade is A")
elif avg>=70:
     print("your grade is B")
elif avg>=60:
     print("your grade is C")
elif avg>=50:
     print("your grade is D")
else:
     print("you ar fail")

