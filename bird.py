from animal import Animal

class Bird(Animal):
    def __init__ (self, age, color):
        super().__init__("Bird", age, color, "Aerial")
           
    def sound(self):
        return "The bird chirps."
                     
                    