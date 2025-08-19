from math import gcd

class Racional:
    def __init__(self, numerador=0, denominador=1):
        if denominador == 0:
            raise ValueError("El denominador no puede ser cero.")
        self.numerador = numerador
        self.denominador = denominador
        self.simplificar()

    def simplificar(self):
        divisor = gcd(self.numerador, self.denominador)
        self.numerador //= divisor
        self.denominador //= divisor

    def leer(self):
        self.numerador = int(input("Numerador: "))
        self.denominador = int(input("Denominador: "))
        self.simplificar()

    def suma(self, otro):
        num = self.numerador * otro.denominador + otro.numerador * self.denominador
        den = self.denominador * otro.denominador
        return Racional(num, den)

    def resta(self, otro):
        num = self.numerador * otro.denominador - otro.numerador * self.denominador
        den = self.denominador * otro.denominador
        return Racional(num, den)

    def multiplicacion(self, otro):
        return Racional(self.numerador * otro.numerador, self.denominador * otro.denominador)

    def division(self, otro):
        return Racional(self.numerador * otro.denominador, self.denominador * otro.numerador)

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"
