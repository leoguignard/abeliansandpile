class AbelianSandPile:
    def __init__(self, *args):
        print("Hello from AbelianSandPile")
        self.arg = args[0]


def run_app():
    my_obj = AbelianSandPile("Hi!")
    print(f"{my_obj.arg = }")
