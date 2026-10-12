"""Act1. Create a class named Car with the following attributes: brand, model and color.
Add a method called show_info() that the full information of the car.
Then, create two objects of the Car class with different value and call the method to display their"""
class car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def show_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Color: {self.color}")

car1 = car("Chevrolet", "Suburban", "Blanco")
car2 = car("Toyota", "Tacoma", "Azul")

car1.show_info()
car2.show_info()