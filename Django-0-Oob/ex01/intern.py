class Intern:
    def __init__(self, name="My name? I'm nobody, an intern, I have no name."):
        self.name = name
    
    def __str__(self):
        return self.name

    def make_coffee(self):
        return self.Coffee()

    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")
    
    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."

intern = Intern()
intern2 = Intern("Mark")


print(f"Hey, intern, what's your name ?\n{intern.__str__()}")
print(f"And you other intern, what's your name ?\n{intern2.__str__()}")

try:
    print(f"Okay no name, can you do my project Piscine-Django ?\n{intern.work()}")
except Exception as e:
    print(e)
try:
    print(f"""Fine... and you, {intern2.__str__()}, can you make me a coffee ?\n\n..Waiting..\n..Waiting..\n..Waiting..\n\n
   `°´ \033[32m( (
       ) )   `°´\033[0m
    ........
    |      |]
    \      /
     `----'
    ( coffee )\n
*{intern2.make_coffee()}*""")
except Exception as e:
    print(e)
    

