# -*- coding: utf-8 -*-
from lettuce import step, world
from calculadora import Calculadora


@step(u'cuando realizo la operacion')
def cuando_realizo_la_operacion(step):
    pass


@step(u'Dado que ingreso los numeros "([^"]*)" y "([^"]*)"')
def dado_que_ingreso_los_numeros_group1_y_group2(step, num1, num2):
    world.cal.suma(int(num1), int(num2))


@step(u'entonces obtengo el resultado "([^"]*)"')
def entonces_obtengo_el_resultado_group1(step, esperado):
    obtenido = world.cal.obtener_resultado()
    try:
        esperado = int(esperado)
    except:
        pass
    assert esperado == obtenido, 'El resultado esperado es ' + \
        str(esperado) + ' y el obtenido es ' + str(obtenido)


@step(u'Dado que meto los numeros "([^"]*)" y "([^"]*)"')
def dado_que_meto_los_numeros_group1_y_group1(step, num1, num2):
    world.cal.resta(int(num1), int(num2))


@step(u'Dado que ingreso los numeros a dividir "([^"]*)" y "([^"]*)"')
def dado_que_ingreso_los_numeros_a_dividir_group1_y_group1(step, num1, num2):
    world.cal = Calculadora()
    world.cal.division(int(num1), int(num2))


@step(u'Dado que ingreso los numeros a multiplicar "([^"]*)" y "([^"]*)"')
def dado_que_ingreso_los_numeros_a_multiplicar_group1_y_group1(
        step,
        num1,
        num2):

    world.cal.multiplicacion(int(num1), int(num2))
