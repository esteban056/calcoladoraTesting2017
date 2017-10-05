Feature: Division de dos numeros
    Como usuario de la calculadora
    deseo dividir dos numeros
    para obtener el resultado preciso
    
    Scenario: division de 2 / 2
        Dado que ingreso los numeros a dividir "2" y "2"
        cuando realizo la operacion
        entonces obtengo el resultado "1"
        
    Scenario: division de 7/5
        Dado que ingreso los numeros a dividir "7" y "5"
        cuando realizo la operacion
        entonces obtengo el resultado "1"
        
    Scenario: division de 0 / -7
        Dado que ingreso los numeros a dividir "0" y "-7"
        cuando realizo la operacion
        entonces obtengo el resultado "0"
        
    Scenario: division de 1000 / 100
        Dado que ingreso los numeros a dividir "1000" y "100"
        cuando realizo la operacion
        entonces obtengo el resultado "10"
        
    Scenario: division de 1 / 0
        Dado que ingreso los numeros a dividir "1" y "0"
        cuando realizo la operacion
        entonces obtengo el resultado "No se puede dividir entre cero"        
        

