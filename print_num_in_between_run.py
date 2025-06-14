from print_num_in_between import NumInBetween
class NibMain:
    def __init__(self):
        self.nib = NumInBetween()
    def NibRun(self):
        while True:
            print("1. Run")
            print("2. End")
            choice = input("Pick (1-2): ")
            if choice == "1":
                self.nib.NibInput()
                self.nib.NibResult()
            else:
                print("Thanks")
                break
nib = NibMain()
nib.NibRun()
