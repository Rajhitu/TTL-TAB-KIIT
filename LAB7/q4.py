# write a pyhton class to reverse a string word by word

class reverse:
    # a=[]

    def __init__(self,word):
        self.a=word
    

    def reverse_it(self):
        for i in range(len(self.a)//2):
            temp=self.a[i]
            self.a[i]=self.a[len(self.a)-i-1]
            self.a[len(self.a)-i-1]=temp
              
    def print_Ans(self):
        print(self.a)

obj=reverse(["hello","world","this","is","hitu"])
obj.reverse_it()
obj.print_Ans()