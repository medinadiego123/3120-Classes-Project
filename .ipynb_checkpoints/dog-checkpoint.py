from animal import Animal

class Dog(Animal):
    def __init__(self, age, color, breed):
        super().__init__("Dog", age, color, "Domestic")
        self.breed = breed

    def sound(self):
        return "The Dog barks."
