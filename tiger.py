from animal import Animal

class Tiger(Animal):
    def __init__(self, age, color):
        super().__init__("Tiger", age, color, "Jungle")

    def sound(self):
        return "The Tiger roars."

    def move(self):
        return "The Tiger is running."
