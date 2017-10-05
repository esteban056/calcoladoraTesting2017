Feature: Resta de dos numeros
    Como usuario de la calculadora
    deseo realizar la resta de dos numeros
    para obtener el resultado preciso
    
    Scenario: resta de 2 - 2
        Dado que meto los numeros "2" y "2"
        cuando realizo la operacion
        entonces obtengo el resultado "0"
        
    Scenario: resta de 7 - 5
        Dado que meto los numeros "7" y "5"
        cuando realizo la operacion
        entonces obtengo el resultado "2"
        
    Scenario: resta de 0 - -7
        Dado que meto los numeros "0" y "-7"
        cuando realizo la operacion
        entonces obtengo el resultado "7"
        
    Scenario: resta de 100 - 1000
        Dado que meto los numeros "100" y "1000"
        cuando realizo la operacion
        entonces obtengo el resultado "-900"
