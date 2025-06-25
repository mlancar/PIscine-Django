class HotBeverage:
    def __init__(self):
        self.price = 0.30
        self.name = "hot beverage"
    
    def description(self):
        return "Just some hot water in a cup"
    
    def __str__(self):
        return (
            f"name : {self.name}\n"
            f"price : {self.price:.2f}\n"
            f"description : {self.description()}"
        )

class Coffee(HotBeverage):
    def __init__(self):
        super().__init__()
        self.name = "coffee"
        self.price = 0.40
    def description(self):
        return "A coffee, to stay awake"

class Tea(HotBeverage):
    def __init__(self):
        super().__init__()
        self.name = "tea"
        self.price = 0.30
    def description(self):
        return "Just some hot water in a cup."

class Chocolate(HotBeverage):
    def __init__(self):
        super().__init__()
        self.name = "chocolate"
        self.price = 0.50
    def description(self):
        return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
    def __init__(self):
        super().__init__()
        self.name = "cappuccino"
        self.price = 0.45
    
    def description(self):
        return "Un po' di Italia nella sua tazza!"

hot_beverage = HotBeverage()
print(hot_beverage.__str__())

coffee = Coffee()
print(f"\n{coffee.__str__()}")

tea = Tea()
print(f"\n{tea.__str__()}")

chocolate = Chocolate()
print(f"\n{chocolate.__str__()}")

cappuccino = Cappuccino()
print(f"\n{cappuccino.__str__()}")
