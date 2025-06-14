class CountEven:
    def __init__(self):
        self.num = 0
        self.even = 0
    def RunCountEven(self):
        for i in range(0, 10):
            self.num = int(input(f"Num {i+1}: "))
            if self.num % 2 == 0:
                self.even += 1
        print(self.even)