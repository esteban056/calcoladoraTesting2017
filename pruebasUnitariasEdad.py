# -*- coding: utf-8 -*-
#Esteban Garcia de Santiago
import unittest

from edad import edad
class CalculadoraTest(unittest.TestCase):
	
	
	def test_edad_negativa(self):
		self.assertEquals(edad(-1),"No existes")
		
	def test_edad_0(self):
		self.assertEquals(edad(0),u"Eres niño")
		
	def test_edad_5(self):
		self.assertEquals(edad(5),u"Eres niño")
	
	def test_edad_13(self):
		self.assertEquals(edad(13),"Eres adolecente")
		
	def test_edad_15(self):
		self.assertEquals(edad(15),"Eres adolecente")
		
	def test_edad_18(self):
		self.assertEquals(edad(18),"Eres adulto")
		
	def test_edad_30(self):
		self.assertEquals(edad(30),"Eres adulto")
		
	def test_edad_65(self):
		self.assertEquals(edad(65),"Eres adulto mayor")
		
	def test_edad_100(self):
		self.assertEquals(edad(100),"Eres adulto mayor")
		
	def test_edad_120(self):
		self.assertEquals(edad(120),"Eres Mumm-Ra")
		
	def test_edad_200(self):
		self.assertEquals(edad(200),"Eres Mumm-Ra")
		
	
if __name__=='__main__':
	unittest.main()