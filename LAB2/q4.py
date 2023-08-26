# same as q3 but using switch case

a = int(input("enter marks of 1st subj "))
b = int(input("enter marks of 2nd subj "))
c = int(input("enter marks of 3rd subj "))
d = int(input("enter marks of 4th subj "))

sum = a+b+c+d
avg = sum/4
print(f"your average marks is {avg}")
a = avg//10
match a:
    case 10:
        print("your grade is O")
    case 9:
        print("your grade is O")
    case 8:
        print("your grade is A")
    case  7:
        print("your grade is B")
    case 6:
        print("your grade is C")
    case 5:
        print("your grade is D")
    case default:
        print("you are fail")



