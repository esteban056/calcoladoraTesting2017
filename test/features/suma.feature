Feature: Suma de dos numeros
    Como usuario de la calculadora
    deseo realizar la suma de dos numeros
    para obtener el resultado preciso
    
    Scenario: suma de 2+2
        Dado que ingreso los numeros "2" y "2"
        cuando realizo la operacion
        entonces obtengo el resultado "4"
        
    Scenario: suma de 7+5
        Dado que ingreso los numeros "7" y "5"
        cuando realizo la operacion
        entonces obtengo el resultado "12"
        
    Scenario: suma de 0 + -7
        Dado que ingreso los numeros "0" y "-7"
        cuando realizo la operacion
        entonces obtengo el resultado "-7"
        
    Scenario: suma de 100 + 1000
        Dado que ingreso los numeros "100" y "1000"
        cuando realizo la operacion
        entonces obtengo el resultado "1100"
