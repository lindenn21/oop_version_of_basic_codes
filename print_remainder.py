class RemainderOnly:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.remainder = 0
    def InputNumRem(self):
        self.num1 = int(input("First num: "))
        self.num2 = int(input("Second num: "))
    def RemResult(self):
        self.remainder = self.num1 % self.num2
        print(self.remainder)