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

    def __str__(self):
        return f"{self.species}, Age: {self.age}, Color: {self.color}, Habitat: {self.habitat}"