class BankAccount:
    # Atributo de clase
    bank = "Central Bank"

    def __init__(self, client, balance):
        self.client = client
        self.balance = balance  

    # Método de instancia
    def show_balance(self):
        print(f"Customer: {self.client} - balance: ${self.balance} USD")

    # Método de clase
    @classmethod
    def show_bank(cls):
        print(f"Bank: {cls.bank}")

    # Método estático
    @staticmethod
    def convert_currency(value):
        # Tipo de cambio fijo: 1 USD = 17.50 MXN
        pesos = value * 17.50
        print(f"${value} USD = ${pesos} MXN")
        return pesos

# Ejemplo de uso
cuenta1 = BankAccount("Juan", 500)

cuenta1.show_balance()          # método de instancia
BankAccount.show_bank()         # método de clase
BankAccount.convert_currency(100)  # método estático