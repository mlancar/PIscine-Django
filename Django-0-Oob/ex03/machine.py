from beverages import *
import random

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"
BRIGHT_MAGENTA = "\033[95m"
ORANGE = "\033[38;5;208m"

class CoffeeMachine:
    def __init__(self):
        self.beverage_serve = 10

    class EmptyCup(HotBeverage):
        def __init__(self):
           super().__init__ ()
           self.name = "empty cup"
           self.price = 0.90
        
        def description(self):
            return f"{ORANGE}empty cup?! Gimme my money back!{RESET}"

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__(f"{RED}This coffee machine has to be repaired.{RESET}")

    def repair(self):
        self.beverage_serve = 10

    def serve(self, HotBeverage):

        if self.beverage_serve == 0:
            raise self.BrokenMachineException()
          
        elif random.randint(1, 2) == 1:
            self.beverage_serve -= 1
            return HotBeverage
        else:
            return self.EmptyCup()


coffeeMachine = CoffeeMachine()
coffee = Coffee()

# cappuccino = Cappuccino()
if __name__ == '__main__':

    for i in range(25):
        try:
            print(f"{YELLOW}*puts {coffee.price:.2f} into the machine*{RESET}")
            served = coffeeMachine.serve(coffee)

            # print(f"{YELLOW}*puts {cappuccino.price:.2f} into the machine*{RESET}")
            # served = coffeeMachine.serve(cappuccino)
            print(f"{BLUE}-{served.description()}\n{RESET}")

        except CoffeeMachine.BrokenMachineException as e:
            print(e)
            coffeeMachine.repair()
            print(f"\n{YELLOW}*** repairing ***")
            print(f"*** repairing ***")
            print(f"*** repairing ***\n{RESET}")
            print(f"{GREEN}Coffee machine is repaired{RESET}\n")