class employee: 
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

class manager(employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary,)
        self.department = department

    def show_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}")

empleado1 = employee("Manuel", 1500)
empleado1.show_info()

manager1 = manager("Laura", 60000, "Networking")
manager1.show_info()