# wap to sort a given dictionary by key


mydic = {"first": 32,
         "second": 2,
         "third": 39,
         "fourth": 2,
         "fifth": 6, 
         }

keys=list(mydic.keys())
keys.sort()

ansdic={}

for i in keys:
    ansdic[i]=mydic[i]
mydic=ansdic
print(mydic)