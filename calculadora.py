# Esteban Garcia de Santiago
class Calculadora(object):

    def __init__(self):
        self.resultado = 0
        self.maxNumero = 10000
        self.msjErrorDatos = 'Datos incorrectos'
        self.msjErrorMaxNum = 'Numero muy grande no se puede computar'
        self.msjErrorDivCero = 'No se puede dividir entre cero'
        self.msjRaizNegativa = 'No se puede calcular numeros imaginarios'

    def obtener_resultado(self):
        return self.resultado

    def suma(self, num1, num2):
        try:
            self.resultado = num1 + num2
        except TypeError:
            self.resultado = self.msjErrorDatos

    def resta(self, num1, num2):
        try:
            self.resultado = num1 - num2
        except TypeError:
            self.resultado = self.msjErrorDatos

    def multiplicacion(self, num1, num2):
        if isinstance(num1, int) and isinstance(num2, int):
            self.resultado = num1 * num2
            if self.resultado > self.maxNumero:
                self.resultado = self.msjErrorMaxNum
        else:
            self.resultado = self.msjErrorDatos

    def division(self, num1, num2):
        try:
            self.resultado = num1 / num2
        except TypeError:
            self.resultado = self.msjErrorDatos
        except ZeroDivisionError:
            self.resultado = self.msjErrorDivCero

    def potencia(self, num1, num2):
        try:
            self.resultado = num1**num2
            if self.resultado > self.maxNumero:
                self.resultado = self.msjErrorMaxNum
        except TypeError:
            self.resultado = self.msjErrorDatos

    def raiz(self, num):
        try:
            if num < 0:
                self.resultado = self.msjRaizNegativa
            else:
                self.resultado = int(num**0.5)
        except TypeError:
            self.resultado = self.msjErrorDatos
