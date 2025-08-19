import random

class Cuenta:
    def __init__(self, dni=0, saldo=0.0, interes_anual=0.0):
        self.numero_cuenta = random.randint(100000000000, 999999999999)
        self.dni = dni
        self.saldo = saldo
        self.interes_anual = interes_anual

    def actualizarSaldo(self):
        interes_diario = self.interes_anual / 365 / 100
        self.saldo += self.saldo * interes_diario

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad

    def mostrar_datos(self):
        print(f"Cuenta: {self.numero_cuenta}")
        print(f"DNI: {self.dni}")
        print(f"Saldo: {self.saldo}")
        print(f"Interés Anual: {self.interes_anual}%")
