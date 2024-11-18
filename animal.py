class Animal:
    def __init__(self, species, age, color, habitat):
        self.species = species
        self.age = age
        self.color = color
        self.habitat = habitat

    def sound(self):
        return f"The {self.species} makes a sound."

    def move(self):
        return f"The {self.species} is moving."

    def eat(self):
        return f"The {self.species} is eating."

my_animal = Animal("Lion", 3, "Golden", "Savanna")
print("Species:",my_animal.species)   
print("Age:",my_animal.age)      
print("Color:",my_animal.color)    
print("Habitat:",my_animal.habitat)   
print(my_animal.sound())  
print(my_animal.move())        
print(my_animal.eat())          