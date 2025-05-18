import beverages
import random

class CoffeeMachine:
    def __init__(self):
        self.beverage_serve = 10

    class EmptyCup(beverages.HotBeverage):
        def __init__(self):
           super().__init__ ()
           self.name = "empty cup"
           self.price = 0.90
        
        def description(self):
            return "empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

    def repair(self):
        self.beverage_serve = 10

    def serve(self, beverage):

        if self.beverage_serve == 0:
            raise self.BrokenMachineException()
          
        elif random.randint(1, 2) == 1:
            self.beverage_serve -= 1
            return beverage
        else:
            return self.EmptyCup()


coffeeMachine = CoffeeMachine()
coffee = beverages.Coffee()

for i in range(25):
    try:
        served = coffeeMachine.serve(coffee)
        print(served.description())
    except CoffeeMachine.BrokenMachineException as e:
        print(e)
    if i == 22:
        coffeeMachine.repair()