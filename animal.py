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

    def sleep(self):
        return f"The {self.species} is sleeping."

    def __str__(self):
        return f"{self.species}, Age: {self.age}, Color: {self.color}, Habitat: {self.habitat}"


class Dog(Animal):
    def __init__(self, age, color, breed):
        super().__init__("Dog", age, color, "Domestic")
        self.breed = breed

    def sound(self):
        return "The Dog barks."


class Tiger(Animal):
    def __init__(self, age, color):
        super().__init__("Tiger", age, color, "Jungle")

    def sound(self):
        return "The Tiger roars."


class Cat(Animal):
    def __init__(self, age, color):
        super().__init__("Cat", age, color, "Domestic")

    def sound(self):
        return "The Cat meows."


def main():
    animals = [
        Dog(5, "Brown", "Golden Retriever"),
        Cat(2, "White"),
        Tiger(4, "Orange")
    ]

    for animal in animals:
        print(animal)
        print(animal.sound())


if __name__ == "__main__":
    main()
