class NumInBetween:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
    def NibInput(self):
        self.num1 = int(input("First num: "))
        self.num2 = int(input("Second num: "))
    def NibResult(self):
        if self.num1 < self.num2:
            print(self.num1, list(range(self.num1 + 1, self.num2)), self.num2)
        else:
            print(self.num2, list(range(self.num2 + 1, self.num1)), self.num1)
