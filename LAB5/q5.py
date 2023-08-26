# wap to multiply all the elements/values present in the dictionary

mydic = {"first": 32,
         "second": 2,
         "third": 39,
         "fourth": 2,
         "fifth": 6, }

ans=1
for i in mydic:
  ans*=mydic[i]

print(f"Multiplication of all the keys present are:{ans}")