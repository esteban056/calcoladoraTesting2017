import unittest

from calculadora import Calculadora
class CalculadoraTest(unittest.TestCase):

	def setUp(self):
		self.calc = Calculadora() 
	
	def test_valor_de_inicio_es_igual_a_cero(self):
		
		self.assertEquals(self.calc.obtener_resultado(),0)
		
	def test_sumar_2_mas_Igual_4(self):
		self.calc.suma(2,2)
		self.assertEquals(self.calc.obtener_resultado(),4)
		
	def test_sumar_3s(self):
		self.calc.suma(3,3)
		self.assertEquals(self.calc.obtener_resultado(),6)
	
	def test_numero_negativo(self):
		self.calc.suma(-1,2)
		self.assertEquals(self.calc.obtener_resultado(),1)
	
	def test_parametro_incorrecto_suma(self):
		self.calc.suma('L',2)
		self.assertEquals(self.calc.obtener_resultado(),'Datos incorrectos')
	
	def test_restar_2_menos_2(self):
		self.calc.resta(2,2)
		self.assertEquals(self.calc.obtener_resultado(),0)
		
	def test_restar_3_menos_4(self):
		self.calc.resta(3,4)
		self.assertEquals(self.calc.obtener_resultado(),-1)
		
	def test_restar_negativos(self):
		self.calc.resta(-2,-3)
		self.assertEquals(self.calc.obtener_resultado(),1)
		
	def test_parametro_incorrecto_resta(self):
		self.calc.resta('R',0)
		self.assertEquals(self.calc.obtener_resultado(),'Datos incorrectos')
	
	def test_multiplicar_2_por_3(self):
		self.calc.multiplicacion(2,3)
		self.assertEquals(self.calc.obtener_resultado(),6)
	
	def test_multiplicar_por_0(self):
		self.calc.multiplicacion(2,0)
		self.assertEquals(self.calc.obtener_resultado(),0)
	
	def test_multiplicar_por_negativo(self):
		self.calc.multiplicacion(2,-5)
		self.assertEquals(self.calc.obtener_resultado(),-10)
		
	def test_multiplicar_numero_mayor_a_10000(self):
		self.calc.multiplicacion(2,10000)
		self.assertEquals(self.calc.obtener_resultado(),'Numero muy grande no se puede computar')
		
	def test_parametro_incorrecto_multiplicacion(self):
		self.calc.multiplicacion('R',3)
		self.assertEquals(self.calc.obtener_resultado(),'Datos incorrectos')
		
	def test_dividir_2_entre_2(self):
		self.calc.division(2,2)
		self.assertEquals(self.calc.obtener_resultado(),1)
		
	def test_dividir_0(self):
		self.calc.division(2,0)
		self.assertEquals(self.calc.obtener_resultado(),'No se puede dividir entre cero')
	
	def test_dividir_entre_negativo(self):
		self.calc.division(10,-2)
		self.assertEquals(self.calc.obtener_resultado(),-5)
	
	def test_dividision_parametro_incorrecto(self):
		self.calc.division(2,'D')
		self.assertEquals(self.calc.obtener_resultado(),'Datos incorrectos')
		
	def test_potencia_2_a_la_2(self):
		self.calc.potencia(2,2)
		self.assertEquals(self.calc.obtener_resultado(),4)
		
	def test_potencia_3_a_la_3(self):
		self.calc.potencia(3,3)
		self.assertEquals(self.calc.obtener_resultado(),27)
		
	def test_potencia_negativo(self):
		self.calc.potencia(-1,2)
		self.assertEquals(self.calc.obtener_resultado(),1)
		
	def test_potencia_parametro_incorrecto(self):
		self.calc.potencia(2,'P')
		self.assertEquals(self.calc.obtener_resultado(),'Datos incorrectos')
		
	def test_potencia_numero_grande(self):
		self.calc.potencia(25,10)
		self.assertEquals(self.calc.obtener_resultado(),'Numero muy grande no se puede computar')
	
	def test_raiz_4(self):
		self.calc.raiz(4)
		self.assertEquals(self.calc.obtener_resultado(),2)
		
	def test_raiz_negativa(self):
		self.calc.raiz(-1)
		self.assertEquals(self.calc.obtener_resultado(),'No se puede calcular numeros imaginarios')
		
	def test_raiz_parametro_incorrecto(self):
		self.calc.raiz('R')
		self.assertEquals(self.calc.obtener_resultado(),'Datos incorrectos')
	def tearDown(self):
		pass
	
if __name__=='__main__':
	unittest.main()