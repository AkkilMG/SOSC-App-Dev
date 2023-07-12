class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("An animal speaks.")


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        print("Bow Bow!")


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow Meow!")


animal = Animal(" Animal", 5)
dog = Dog("German Shepard", 3, "Labrador")
cat = Cat("Kitty", 2, "Prussian")

print("Animal:", animal.name)
print("Age:", animal.age)
animal.speak()

print("\nDog:", dog.name)
print("Age:", dog.age)
print("Breed:", dog.breed)
dog.speak()

print("\nCat:", cat.name)
print("Age:", cat.age)
print("Color:", cat.color)
cat.speak()

# OUTPUT
# Animal:  Animal
# Age: 5
# An animal speaks.
# Dog: German Shepard
# Age: 3
# Breed: Labrador
# Bow Bow!
# Cat: Kitty
# Age: 2
# Color: Prussian
# Meow Meow!
