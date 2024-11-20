from animal import Animal

class Cat(Animal):
    def __init__(self, age, color):
        super().__init__("Cat", age, color, "Domestic")

    def sound(self):
        return "The Cat meows."