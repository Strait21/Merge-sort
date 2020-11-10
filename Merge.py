import random

class Merge:
    def __init__(self):
        self.stuff = []
        self.length = 0

    def contents(self):
        print(self.stuff)

    def add(self, int):
        self.stuff.append(int)
        self.length += 1

    def left_vs_right(self, left, right):
        i = 0
        j = 0
        k = 0
        while i < len(leftarray) and j < len(rightarray):
                if leftarray[i] <= rightarray[j]:
                    self.stuff[k] = leftarray[i]
                    i +=1    
                else:
                    self.stuff[k] = rightarray[j]
                    j +=1
                k += 1
        while i < len(leftarray):
                self.stuff[k] = leftarray[i]
                i += 1
                k += 1
        while j < len(rightarray):
            self.stuff[k] = rightarray[j]
            j += 1
            k += 1
    def mergeSort(self,arr):
        if len(arr.stuff) >= 1:
            middle = self.length // 2

            leftarray = self.stuff[:middle]
            rightarray = self.stuff[middle:]

            self.mergeSort(leftarray)
            self.mergeSort(rightarray)

            self.left_vs_right(leftarray,rightarray)


m1 = Merge()

for x in range(50):
    m1.add(random.randint(1,100))
m1.contents()

m1.mergeSort(m1)

m1.contents()

            

            




