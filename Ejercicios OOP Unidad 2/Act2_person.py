class person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def greet(self):
        print(f"Hi, mi name is {self.name}, I am {self.age} years old, and I lived in {self.city}.")

person1 = person("Juan", 15, "Guadalajara")
person2 = person("Maria", 22, "Tijuana")
person3 = person("Mateo", 18, "Culiacan")

person1.greet()
person2.greet()
person3.greet()