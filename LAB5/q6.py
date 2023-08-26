# wap to mergee to dictionary

mydic1 = {"first": 32,
         "second": 2,
         "third": 39,
         "fourth": 2,
         "fifth": 6, }

mydic2 = {"naeme":"hitu",
         "roll": 25,
         "class": 10,
          }

mydic1.update(mydic2)
# for  i in mydic2:
#     mydic1.add({i,mydic2[i]})
print("after merging:")
print(mydic1)