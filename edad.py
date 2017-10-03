# -*- coding: utf-8 -*-
#Esteban Garcia de Santiago
def edad(edad):
	mensaje = "Eres Mumm-Ra"

	if edad < 120:
		mensaje = "Eres adulto mayor"
	if edad < 65:
		mensaje = "Eres adulto"
	if edad < 18:
		mensaje = "Eres adolecente"	
	if edad < 13:
		mensaje = u"Eres niño"
	if edad < 0:
		mensaje = "No existes"

	return mensaje