

    # [" CRIADOR: LUIZ ÂNGELO MARTINS "]:
	 
    # DESCRIÇÃO:
    # PROJETO DE SISTEMA DE ESTACIONAMENTO QUE CONSISTE EM:		
    # CALCULAR O TEMPO E O TOTAL A PAGAR PARA MOTOS,
    # CALCULAR O TEMPO E O TOTAL A PAGAR PARA CARROS.
	
    # COMPILADOR USADO:
    # IDLE PYTHON


# DECLARAÇÃO DE VARIAVEIS:
repetir = 0
escolha_usuario = 0
aux1 = 0
valor_hora = 0
hora_inicial = 0
hora_final = 0
hora_resultado1 = 0
hora_resultado2 = 0
    
while repetir < 1:

    try:

        #ZERANDO VALORES:
        repetir = 0
        escolha_usuario = 0
        aux1 = 0
        valor_hora = 0
        hora_inicial = 0
        hora_final = 0
        hora_resultado1 = 0
        hora_resultado2 = 0
    
        print("\n")
        print("	MENU GERAL - CALCULOS:")
        print("")
        print("	0 - SAIR")
        print("	1 - CARRO")
        print("	2 - MOTO \n")
        escolha_usuario = int(input("	DIGITE SUA RESPOSTA: "))
	
	# "FILTRAGEM DA ESCOLHA DO USUARIO":
        # CASO "0" - SAIR:
        if escolha_usuario == 0:
            exit()
                
        # CASO "1" - CARRO:
        if escolha_usuario == 1:

            #ZERANDO VALORES:
            valor_hora = 0.0
            hora_inicial = 0.0
            hora_final = 0.0
                 
            # ORIENTAÇÃO:
            print("\n")
            print("	CALCULO DO TEMPO - CARRO:")
            print("	OBS: SEPARE OS VALORES COM PONTO")
			        
	    # VALOR DA HORA:
	    # HORARIO DE ENTRADA:
	    # HORARIO DE SAÍDA:
            print("\n")
            valor_hora = float(input("	DIGITE O VALOR DA HORA: "))
            hora_inicial = float(input("	DIGITE O HORARIO DE ENTRADA: "))
            hora_final = float(input("	DIGITE O HORARIO DE SAIDA: "))

            # CALCULO:
            hora_resultado1 = hora_final - hora_inicial
            hora_resultado2 = hora_resultado1*valor_hora
            aux1 = hora_resultado2

            # ARREDONDAMENTO DE VALORES:
            hora_resultado1 = round(hora_resultado1,2)
            hora_resultado2 = round(hora_resultado2,2)
            aux1 = round(aux1,2)

	    # EXIBIÇÃO:
            print("\n")
            print("	TOTAL DE HORAS: ", hora_resultado1)
            print("	VALOR BRUTO: ", aux1)
            print("	TOTAL A PAGAR: R$ ", hora_resultado2);

        # CASO "2" - MOTO:
        if escolha_usuario == 2:

            #ZERANDO VALORES:
            valor_hora = 0.0
            hora_inicial = 0.0
            hora_final = 0.0
                 
            # ORIENTAÇÃO:
            print("\n")
            print("	CALCULO DO TEMPO - MOTO:")
            print("	OBS: SEPARE OS VALORES COM PONTO")
			        
	    # VALOR DA HORA:
	    # HORARIO DE ENTRADA:
	    # HORARIO DE SAÍDA:
            print("\n")
            valor_hora = float(input("	DIGITE O VALOR DA HORA: "))
            hora_inicial = float(input("	DIGITE O HORARIO DE ENTRADA: "))
            hora_final = float(input("	DIGITE O HORARIO DE SAIDA: "))

            # CALCULO:
            hora_resultado1 = hora_final - hora_inicial
            hora_resultado2 = hora_resultado1*valor_hora
            aux1 = hora_resultado2

            # ARREDONDAMENTO DE VALORES:
            hora_resultado1 = round(hora_resultado1,2)
            hora_resultado2 = round(hora_resultado2,2)
            aux1 = round(aux1,2)

	    # EXIBIÇÃO:
            print("\n")
            print("	TOTAL DE HORAS: ", hora_resultado1)
            print("	VALOR BRUTO: ", aux1)
            print("	TOTAL A PAGAR: R$ ", hora_resultado2);

        # "EM CASO DE VALORES INVALIDOS":
        if escolha_usuario != 0 and escolha_usuario != 1 and escolha_usuario != 2:

            print("\n        POR FAVOR DIGITE UM VALOR VALIDO!")
            print("        TENTE NOVAMENTE!")
	    
    except Exception:

        print("\n        ERRO!")
        print("        POR FAVOR TENTE NOVAMENTE!")




