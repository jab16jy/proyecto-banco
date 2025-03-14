class Banco:
    def __init__(self):
        self.saldo = 0

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            return True, f"Has depositado ${cantidad:.2f}."
        else:
            return False, "Error: La cantidad debe ser mayor a 0."

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            return False, "Saldo insuficiente."
        elif cantidad > 0:
            self.saldo -= cantidad
            return True, f"Has retirado ${cantidad:.2f}."
        else:
            return False, "Error: La cantidad debe ser mayor a 0."

    def consultar_saldo(self):
        return f"Tu saldo es: ${self.saldo:.2f}"