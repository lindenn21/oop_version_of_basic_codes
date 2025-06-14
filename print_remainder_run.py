from print_remainder import RemainderOnly
class RemMain:
    def __init__(self):
        self.run_rem = RemainderOnly()
    def RemMenu(self):
        while True:
            print("1. Run")
            print("2. End")
            choice = input("Input your choice:")
            if choice == "1":
                self.run_rem.InputNumRem()
                self.run_rem.RemResult()
            else:
                print("Thanks!")
                break
rem = RemMain()
rem.RemMenu()