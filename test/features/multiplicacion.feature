Feature: Multiplicacion de dos numeros
    Como usuario de la calculadora
    deseo multiplicar dos numeros
    para obtener el resultado preciso
    
    Scenario: multiplicacion de 2 * 2
        Dado que ingreso los numeros a multiplicar "2" y "2"
        cuando realizo la operacion
        entonces obtengo el resultado "4"
        
    Scenario: suma de 7 * 5
        Dado que ingreso los numeros a multiplicar "7" y "5"
        cuando realizo la operacion
        entonces obtengo el resultado "35"
        
    Scenario: suma de 0 * -7
        Dado que ingreso los numeros a multiplicar "0" y "-7"
        cuando realizo la operacion
        entonces obtengo el resultado "0"
        
    Scenario: suma de 100 * 1000
        Dado que ingreso los numeros a multiplicar "100" y "1000"
        cuando realizo la operacion
        entonces obtengo el resultado "100000"
