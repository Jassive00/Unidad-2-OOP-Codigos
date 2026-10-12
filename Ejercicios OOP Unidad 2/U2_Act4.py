class Motor:
    def arrancar(self):
        print("Motor encendido")

class Auto:
    def __init__(self, motor):
        self.motor = motor

    def arrancar_auto(self):
        self.motor.arrancar()

motor = Motor()
auto1 = Auto(motor)
auto1.arrancar_auto()
