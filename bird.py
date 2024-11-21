from animal import Animal

class Bird(Animal):
    def  __init__(self, age, color, type,  breed):
         super().__init__("Bird", age, color, "Wild") 

    def move(self):
         return "The Bird is flying."

    def sound(self):
        return "The Bird chirps."
