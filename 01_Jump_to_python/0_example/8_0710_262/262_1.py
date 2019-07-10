class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value = self.value + val
class UpgradeCalculator(Calculator):
    def minus(self, val2):
        self.value = self.value - val2

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)