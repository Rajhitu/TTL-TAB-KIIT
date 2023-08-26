# write a pyhton class or program to print all possible unique subsets from set of integers


class findSubsets:
    # nums=[]
    # subsets=[]

    def __init__(self, nums):
        self.nums = nums
        self.subsets = []

    def giveSubsets(self):
        n = len(self.nums)
        for i in range(2 ** n):
            subset = []
            for j in range(n):
                if i & (1 << j):
                    subset.append(self.nums[j])
            if subset not in self.subsets:
                self.subsets.append(subset)
            
    
        return self.subsets


myset = [1,2,3]
ans = findSubsets(myset)
print("ALL unique subsets from sets are:\t", ans.giveSubsets())
