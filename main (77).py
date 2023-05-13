class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        
    def bark(self):
        print(f"{self.name} says woof!")
        
    def fetch(self, item):
        print(f"{self.name} fetched the {item}!")
        
my_dog = Dog("Rufus", "Golden Retriever", 5)
my_dog.bark()
my_dog.fetch("ball")
