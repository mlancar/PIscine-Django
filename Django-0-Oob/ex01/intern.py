class Coffee:
    def __str__(self):
        return "This is the worst coffee you ever tasted."

class Intern:
    def __init__(self, coffee, name="My name? I'm nobody, an intern, I have no name."):
        self.name = name
        self.coffee = coffee
    
    def __str__(self):
        return self.name

    def make_coffee(self):
        return Coffee()

    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")


coffee = Coffee()

intern = Intern(coffee)
intern2 = Intern(coffee, "Mark")


print("What's your name ?\n", intern.__str__())
print("AndWhat's your name ?\n", intern2.__str__())

try:
    print("Hey no name, can you do my project Piscine-Django ?\n", intern.work())
except Exception as e:
    print(e)
try:
    print("Hey", intern2.__str__(), ", can you make me a coffee ?\n...Waiting...\n...Waiting...\n...Waiting...\n", intern2.make_coffee())
except Exception as e:
    print(e)
    

