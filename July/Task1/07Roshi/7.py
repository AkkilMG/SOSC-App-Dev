class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        pass

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        return "Woof!"

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        return "Meow!"

dog = Dog("Buddy", 3, "Labrador")
cat = Cat("Whiskers", 5, "Gray")

print(f"{dog.name} is a {dog.breed} and says {dog.speak()}")
print(f"{cat.name} is {cat.age} years old, has {cat.color} fur, and says {cat.speak()}")


"""OutPut:
Buddy is a Labrador and says Woof!
Whiskers is 5 years old, has Gray fur, and says Meow! """