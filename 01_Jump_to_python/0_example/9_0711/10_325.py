number = []
class Calculator:
    def __init__(self,number):
        self.number = number
        self.result = 0
        self.average = 0
        self.count = 0
    def sum(self):
        for index in self.number:
            self.result = self.result + index
            self.count = self.count + 1
        print(self.result)
    def avg(self):
        self.average = self.result / self.count
        print(self.average)
cal1 = Calculator([1,2,3,4,5])
cal1.sum()
cal1.avg()
cal2 = Calculator([6,7,8,9,10])
cal2.sum()
cal2.avg()

