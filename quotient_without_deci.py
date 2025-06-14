class QuotientNoDeci:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.quotient = 0
    def RunQnd(self):
        self.num1 = int(input("First num: "))
        self.num2 = int(input("Second num: "))
        self.quotient = self.num1 // self.num2
        print(self.quotient)