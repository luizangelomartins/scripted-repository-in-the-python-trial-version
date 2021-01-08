


    # [" CRIADOR: LUIZ ÂNGELO MARTINS "]:

    # DESCRIÇÃO:
    # PROJETO DE CALCULOS QUE CONSISTE EM:	
    # - CALCULO DE MMC,
    # - SOMAR FRAÇÃO,
    # - SUBTRAIR FRAÇÃO,
    # - MULTIPLICAR FRAÇÃO,
    # - DIVIDIR FRAÇÃO,
    # - CALCULO DE IMC,
    # - CONVERTER CELSIUS PARA KELVIN,
    # - CELSIUS PARA FAHRENHEIT,
    # - KELVIN PARA CELSIUS,
    # - KELVIN PARA FAHRENHEIT,
    # - FAHRENHEIT PARA CELSIUS,
    # - FAHRENHEIT PARA KELVIN.

    # COMPILADOR USADO:
    # IDLE PYTHON


# IMPORTAÇÃO DE BIBLIOTECAS:
import math


# DECLARAÇÃO DE VARIAVEIS E OBJETOS:
escolha_usuario = 1
denominador1 = 0
denominador2 = 0
resultado = 0
a = 0
b = 0
denominador_soma = 0
numerador1_soma = 0
numerador2_soma = 0
numerador2 = 0
result1 = 0
result2 = 0
denominador1_multiplicar = 0
denominador2_multiplicar = 0
numerador1_multiplicar = 0
numerador2_multiplicar = 0
numerador = 0
denominador = 0
result = 0
denominador1_dividir = 0
denominador2_dividir = 0
numerador1_dividir = 0
numerador2_dividir = 0
        
        
# "FILTRAGEM DE ESCOLHAS":
while escolha_usuario > 0:

    try:
            
        # "ZERANDO VALORES":
        denominador1_dividir = 0
        denominador2_dividir = 0
        numerador1_dividir = 0
        numerador2_dividir = 0
        escolha_usuario = 1
        denominador1 = 0
        denominador2 = 0
        resultado = 0
        a = 0
        b = 0
        denominador_soma = 0
        numerador1_soma = 0
        numerador2_soma = 0
        numerador2 = 0
        result1 = 0
        result2 = 0
        denominador1_multiplicar = 0
        denominador2_multiplicar = 0
        numerador1_multiplicar = 0
        numerador2_multiplicar = 0
        numerador = 0
        denominador = 0
        result = 0
            
        # MENU:
        print("")
        print("	MENU GERAL - CALCULADORA: \n")
        print("	0 = SAIR.")
        print("	1 = CALCULO DE MMC.")
        print("	2 = SOMAR FRACAO.")
        print("	3 = SUBTRAIR FRACAO.")
        print("	4 = MULTIPLICAR FRACAO.")
        print("	5 = DIVIDIR FRACAO.")
        print("	6 = CALCULO DE IMC.")
        print("	7 = CONVERTER CELSIUS PARA KELVIN.")
        print("	8 = CONVERTER CELSIUS PARA FAHRENHEIT.")
        print("	9 = CONVERTER KELVIN PARA CELSIUS.")
        print("	10 = CONVERTER KELVIN PARA FAHRENHEIT.")
        print("	11 = CONVERTER FAHRENHEIT PARA CELSIUS.")
        print("	12 = CONVERTER FAHRENHEIT PARA KELVIN.")
        print("")
        escolha_usuario = int(input("	DIGITE SUA RESPOSTA: "))
        
        # BLOCO QUE SE TRATA DO ENCERRAMENTO DO PROGRAMA:
        if escolha_usuario == 0:
            exit()
                
        # BLOCO QUE SE TRATA DO MMC:
        if escolha_usuario == 1:

            print("")	
            print("	CALCULO DE MMC.")
            print("")
            denominador1 = int(input("	Digite o primeiro MMC: "))
            denominador2 = int(input("	Digite o segundo MMC: "))

            a = denominador1
            b = denominador2

            while b != 0:
		        
                r = a % b
                a = b
                b = r

            resultado = denominador1 * (denominador2 / a )
            print("")
            print("	O MMC DE", denominador1, "E", denominador2, "E:", resultado)

        # BLOCO QUE SE TRATA DA SOMA DE FRAÇÕES:
        if escolha_usuario == 2:
            
            while denominador_soma < 1:
                    
                print("")
                print("	SOMA DE FRACOES.")
                print("")
                denominador_soma = int(input("	Digite o denominador: "))
                numerador1_soma = int(input("	Digite o primeiro numerador: "))
                numerador2_soma = int(input("	Digite o segundo numerador: "))

                if denominador_soma == 0:
							
                    print("")
                    print("	O DENOMINADOR NAO PODE SER ZERO!")
                    
                result1 = numerador1_soma + numerador2_soma
                result2 = result1 / denominador_soma
                print("")
                print("	SUA FRACAO:", (numerador1_soma + numerador2_soma), "/", denominador_soma)
                print("	A APROXIMACAO DEU:", result2)

        # BLOCO QUE SE TRATA DA SUBTRAÇÃO DE FRAÇÕES:
        if escolha_usuario == 3:
            
            while denominador_soma < 1:
                    
                print("")
                print("	SUBTRACAO DE FRACOES.")
                print("")
                denominador_soma = int(input("	Digite o denominador: "))
                numerador1_soma = int(input("	Digite o primeiro numerador: "))
                numerador2_soma = int(input("	Digite o segundo numerador: "))

                if denominador_soma == 0:
							
                    print("")
                    print("	O DENOMINADOR NAO PODE SER ZERO!")

                result1 = numerador1_soma - numerador2_soma
                result2 = result1 / denominador_soma
                print("")
                print("	SUA FRACAO:", (numerador1_soma - numerador2_soma), "/", denominador_soma)
                print("	A APROXIMACAO DEU:", result2)

        # BLOCO QUE SE TRATA DA MULTIPLICAÇÃO DE FRAÇÕES:
        if escolha_usuario == 4:
           
            while denominador1_multiplicar == 0 or denominador1_multiplicar == 1 or denominador2_multiplicar == 0 or denominador2_multiplicar == 1:
            
                print("")
                print("	MULTIPLICACAO DE FRACOES.")
                print("")
                denominador1_multiplicar = int(input("	Digite o primeiro denominador: "))
                denominador2_multiplicar = int(input("	Digite o segundo denominador: "))
                numerador1_multiplicar = int(input("	Digite o primeiro numerador: "))
                numerador2_multiplicar = int(input("	Digite o segundo numerador: "))
                print("")

                if denominador1_multiplicar == 0:
                    print("	DENOMINADOR 1 - NAO HA SUPORTE PARA ESTE DENOMINADOR!")

                if denominador2_multiplicar == 0:
                    print("	DENOMINADOR 2 - NAO HA SUPORTE PARA ESTE DENOMINADOR!")

                if denominador1_multiplicar == 1:
                    print("	DENOMINADOR 1 - NAO HA SUPORTE PARA ESTE DENOMINADOR!")

                if denominador2_multiplicar == 1:
                    print("	DENOMINADOR 2 - NAO HA SUPORTE PARA ESTE DENOMINADOR!")

                numerador = numerador1_multiplicar * numerador2_multiplicar
                denominador = denominador1_multiplicar * denominador2_multiplicar
                result = numerador / denominador
                print("	SUA FRACAO:", numerador, "/", denominador)
                print("	A APROXIMACAO DEU:", result)

        # BLOCO QUE SE TRATA DA DIVISÃO DE FRAÇÕES:
        if escolha_usuario == 5:
            
            while denominador1_dividir == 0 or denominador2_dividir == 0:
                		
                print("")
                print("	DIVISAO DE FRACOES.")
                print("")
                numerador1_dividir = int(input("	Digite o primeiro numerador: "))
                numerador2_dividir = int(input("	Digite o segundo numerador: "))
                denominador1_dividir = int(input("	Digite o primeiro denominador: "))
                denominador2_dividir = int(input("	Digite o segundo denominador: "))
                print("")
	                
                if denominador1_dividir == 0:
                    print("	DENOMINADOR 1 - NAO HA SUPORTE PARA ESTE DENOMINADOR!")

                if denominador2_dividir == 0:
                    print("	DENOMINADOR 2 - NAO HA SUPORTE PARA ESTE DENOMINADOR!")

                numerador = numerador1_dividir * denominador2_dividir
                denominador = denominador1_dividir * numerador2_dividir
                result = numerador / denominador
                print("	SUA FRACAO:", numerador, "/", denominador )
                print("	A APROXIMACAO DEU:", result)

        # BLOCO QUE TRATA SOBRE O IMC:
        if escolha_usuario == 6:
                
            peso = 0.0
            altura = 0.0
            result = 0.0
            resultado_imc = 0.0
                
            print("")	
            print("	IMC.")        
            peso = float(input("	Digite o valor do peso corporal: "))
            altura = float(input("	Digite o valor da altura: "))

            resultado = peso / ( altura * altura )
            result = resultado
            result = round(result,2)
            print("")
            print("	IMC =", result);
                
            if result < 18:
                print("	A PESSOA ESTA ABAIXO DO PESO!")

            if result > 18 and result < 25:
                print("	A PESSOA ESTA COM O PESO NORMAL!")

            if result > 25 and result < 30:
                print("	A PESSOA ESTA COM SOBRE PESO!")

            if result > 30 and result < 35:
                print("	A PESSOA ESTA COM OBESIDADE GRAU I!")

            if result > 35 and result < 40:
                print("	A PESSOA ESTA COM OBESIDADE GRAU II!")

            if result > 40:
                print("	A PESSOA ESTA COM OBESIDADE GRAU III!")

        # MÉTODO PARA O CÁLCULO DE TEMPERATURA:
        # CELSIUS PARA KELVIN:
        if escolha_usuario == 7:
              
            celcius = 0.0
            kelvin = 0.0
		        
            print("")
            print("	CELSIUS PARA KELVIN.")    
            celcius = float(input("	Digite o valor da temperatura em celsius: "))
            kelvin = celcius + 273.15
            kelvin = round(kelvin,2)
            print("")
            print("	A TEMPERATURA DE", celcius, "GRAUS CELSIUS E IGUAL A", kelvin, "KELVIN")

        # MÉTODO PARA O CÁLCULO DE TEMPERATURA:
        # CELSIUS PARA FAHRENHEIT:
        if escolha_usuario == 8:
         
            celsius_Fahrenheit = 0.0
            Fahrenheit = 0.0
                
            print("")
            print("	CELSIUS PARA FAHRENHEIT.")   
            celsius_Fahrenheit = float(input("	Digite o valor da temperatura em celsius: "))
            Fahrenheit = ( celsius_Fahrenheit * 9/5 ) + 32
            Fahrenheit = round(Fahrenheit,2)
            print("")
            print("	A TEMPERATURA DE", celsius_Fahrenheit, "GRAUS CELSIUS E IGUAL A", Fahrenheit, "FAHRENHEIT")

        # MÉTODO PARA O CÁLCULO DE TEMPERATURA:
        # KELVIN PARA CELSIUS:
        if escolha_usuario == 9:
                
            kelvin_Celcius = 0.0
            celcius_kelvin = 0.0
                
            print("")
            print("	KELVIN PARA CELSIUS.")	
            kelvin_Celcius = float(input("	Digite o valor da temperatura em kelvin: "))
            celcius_kelvin = kelvin_Celcius - 273.15
            celcius_kelvin = round(celcius_kelvin,2)
            print("")
            print("	A TEMPERATURA DE", kelvin_Celcius, "KELVIN E IGUAL A", celcius_kelvin, "CELCIUS")

        # MÉTODO PARA O CÁLCULO DE TEMPERATURA:
        # KELVIN PARA FAHRENHEIT:
        if escolha_usuario == 10:
                
            kelvin_Fahrenheit = 0.0
            Fahrenheit_from_kelvin = 0.0
                
            print("")	
            print("	KELVIN PARA FAHRENHEIT.")
            kelvin_Fahrenheit = float(input("	Digite o valor da temperatura em kelvin: "))
            Fahrenheit_from_kelvin = ( kelvin_Fahrenheit - 273.15 ) * 9/5 + 32
            Fahrenheit_from_kelvin = round(Fahrenheit_from_kelvin,2)
            print("")
            print("	A TEMPERATURA DE", kelvin_Fahrenheit, "KELVIN E IGUAL A", Fahrenheit_from_kelvin, "FAHRENHEIT")

        # MÉTODO PARA O CÁLCULO DE TEMPERATURA:
        # FAHRENHEIT PARA CELSIUS:
        if escolha_usuario == 11:
                
            fahrenheit_Celcius = 0.0
            Celcius_from_Fahrenheit = 0.0
                
            print("")	
            print("	FAHRENHEIT PARA CELSIUS.")	
            fahrenheit_Celcius = float(input("	Digite o valor da temperatura em fahrenheit: "))
            Celcius_from_Fahrenheit = ( fahrenheit_Celcius - 32 ) * 5/9
            Celcius_from_Fahrenheit = round(Celcius_from_Fahrenheit,2)
            print("")
            print("	A TEMPERATURA DE", fahrenheit_Celcius, "FAHRENHEIT E IGUAL A", Celcius_from_Fahrenheit, "CELSIUS")

        # MÉTODO PARA O CÁLCULO DE TEMPERATURA:
        # FAHRENHEIT PARA KELVIN:
        if escolha_usuario == 12:
                
            fahrenheit_Kelvin = 0.0
            Kelvin_from_Fahrenheit = 0.0
                
            print("")	
            print("	FAHRENHEIT PARA KELVIN.")
            fahrenheit_Kelvin = float(input("	Digite o valor da temperatura em fahrenheit: "))
            Kelvin_from_Fahrenheit = ( fahrenheit_Kelvin - 32 ) * 5/9 + 273.15
            Kelvin_from_Fahrenheit = round(Kelvin_from_Fahrenheit,2)    
            print("")	
            print("	A TEMPERATURA DE", fahrenheit_Kelvin, "FAHRENHEIT E IGUAL A", Kelvin_from_Fahrenheit, "KELVIN")
                
        # VALORES INVALIDOS:
        if escolha_usuario != 0 and escolha_usuario != 1 and escolha_usuario != 2 and escolha_usuario != 3 and escolha_usuario != 4 and escolha_usuario != 5 and escolha_usuario != 6 and escolha_usuario != 7 and escolha_usuario != 8 and escolha_usuario != 9 and escolha_usuario != 10 and escolha_usuario != 11 and escolha_usuario != 12:

            print("")
            print("	VALOR INVALIDO!")
            print("	POR FAVOR TENTE NOVAMENTE!")
		
    except Exception:

        print("\n        ERRO!")
        print("        POR FAVOR TENTE NOVAMENTE!")




