

    # [" CRIADOR: LUIZ ÂNGELO MARTINS "]:

    # DESCRIÇÃO:
        #PROJETO DE "TIMER/TEMPORIZADOR" QUE CONSISTE EM:
	# CRONOMETRAR,
	# TEMPORIZAR.
		
    # COMPILADOR USADO:
        # IDLE PYTHON


# IMPORTAÇÃO DE BIBLIOTECAS:
import time
from random import randint
#time.sleep(0.3)
#print(len(vetor_numero))


# DECLARAÇÃO DE VARIAVEIS "INTEIRAS":
repetir = 0
repetir2 = 0
repetir3 = 0
escolha_usuario = 0
escolha_usuario2 = 0
escolha_usuario3 = 0
aux1 = 0
aux2 = 0
tempo2 = 0
tempo3 = 0
tempo4 = 0
tempo5 = 0
tempo6 = 0
tempo_aux1 = 0
tempo_aux2 = 0
tempo_aux3 = 0
    
while repetir < 1:

    try:
              
        #ZERANDO VALORES:
        repetir = 0
        escolha_usuario = 0
        escolha_usuario2 = 0
        escolha_usuario3 = 0
        aux1 = 0
        aux2 = 0
        tempo2 = 0
        tempo3 = 0
        tempo4 = 0
        tempo5 = 0
        tempo6 = 0
        repetir2 = 0
        
        # EXIBIÇÃO DO MENU:   
        print("\n")
        print("	MENU - GERAL:")
        print("")       
        print("	0 - SAIR.")
        print("	1 - CRONOMETRO.")
        print("	2 - TEMPORIZADOR. \n")
        escolha_usuario = int(input("	DIGITE SUA RESPOSTA: "))

        # "FILTRAGEM DA ESCOLHA DO USUARIO":
        # CASO "0" - SAIR:
        if escolha_usuario == 0:
            exit()

        # CASO "1" - CRONOMETRO:
        if escolha_usuario == 1:
                           
            repetir2 = 0
            tempo_aux1 = 0
            tempo_aux2 = 0
            tempo_aux3 = 0
            
            while repetir2 < 1:
                    
                # EXIBIÇÃO DO MENU DO CRONOMETRO:			
                print("\n")
                print("	MENU - CRONOMETRO")	                
                print("	TEMPO LIMITE: 10 ( DEZ ) HORAS")
                print("")	                
                print("	0 - VOLTAR AO MENU PRINCIPAL.")
                print("	1 - INICIAR CONTAGEM.")
                print("	2 - ACERTAR O TEMPO. \n")               
                escolha_usuario2 = int(input("	DIGITE SUA RESPOSTA: "))

                # "FILTRAGEM DA ESCOLHA DO USUARIO":
                # CASO "0" - SAIR:
                if escolha_usuario2 == 0:
                    repetir2 = 1
                                                
                            
                # CASO "1" - INICIAR CONTAGEM:
                if escolha_usuario2 == 1:
                                                    
                    print("")
                    aux1 = 0
                    aux2 = 1
                    print("	CONTAGEM:")	
                                                                    
                    while aux2 < 3:
                                		        	
                        print("	CRONOMETRO - ", tempo2,"h:",tempo3,tempo4,"m:",tempo5,tempo6,"s")
                        tempo6 = tempo6 + 1
                                                            
                        # SEGUNDOS:
                        if tempo6 > 9:
                            tempo6 = 0
                            tempo5 = tempo5 + 1
                                
                        if tempo5 > 5:
                            tempo5 = 0
                            tempo4 = tempo4 + 1
                                            
                        # MINUTOS:
                        if tempo4 > 9:
                            tempo4 = 0
                            tempo3 = tempo3 + 1
                            
                        if tempo3 > 5:
                            tempo3 = 0
                            tempo2 = tempo2 + 1
                                            
                        # HORAS:
                        if tempo2 > 9:
                            tempo6 = 0
                            tempo5 = 0
                            tempo4 = 0
                            tempo3 = 0
                            tempo2 = 0
                            break
                                
                        time.sleep(1.0)

                                    
                # CASO "2" - ACERTAR O TEMPO:
                if escolha_usuario2 == 2:
                                                                                            
                    print("\n")
                    print("	DEFINIR TEMPO:")
            
                    # SEGUNDOS:
                    while tempo_aux1 < 1:

                        print("\n	SEGUNDOS:")
                        tempo6 = int(input("	DIGITE OS SEGUNDOS PARTE 1 - ( 0 - 9 ): "))
                        tempo5 = int(input("	DIGITE OS SEGUNDOS PARTE 2 - ( 0 - 5 ): "))
                                                                        
                        if tempo6 < 10 and tempo5 < 6:
                            tempo_aux1 = 1
                                                                    
                    # MINUTOS:
                    while tempo_aux2 < 1:
                        
                        print("\n	MINUTOS:")			            
                        tempo4 = int(input("	DIGITE OS MINUTOS PARTE 1 - ( 0 - 9 ): "))
                        tempo3 = int(input("	DIGITE OS MINUTOS PARTE 2 - ( 0 - 5 ): "))

                        if tempo4 < 10 and tempo3 < 6:
                            tempo_aux2 = 1
                                                                    
                    # HORAS:
                    while tempo_aux3 < 1:
                        
                        print("\n	HORAS:")
                        tempo2 = int(input("	DIGITE AS HORAS PARTE 1 - ( 0 - 9 ): "))
                            
                        if tempo2 < 10:
                            tempo_aux3 = 1
                                                                        
                                                                    
                                                
                # "EM CASO DE VALORES INVALIDOS":
                if escolha_usuario2 != 0 and escolha_usuario2 != 1 and escolha_usuario2 != 2:

                    print("\n        POR FAVOR DIGITE UM VALOR VALIDO!")
                    print("        TENTE NOVAMENTE!")
                            
                        
        # CASO "2" - TEMPORIZADOR:
        if escolha_usuario == 2:
                            
            repetir3 = 0
            tempo_aux1 = 0
            tempo_aux2 = 0
            tempo_aux3 = 0
            
            while repetir3 < 1:
                                                
                print("\n")	                
                print("	MENU - TEMPORIZADOR")
                print("	TEMPO LIMITE: 10 ( DEZ ) HORAS")
                print("")	                
                print("	0 - VOLTAR AO MENU PRINCIPAL.")
                print("	1 - ACERTAR O TEMPO E INICIAR CONTAGEM. \n")               
                escolha_usuario3 = int(input("	DIGITE SUA RESPOSTA: "))

                                 
                # "FILTRAGEM DA ESCOLHA DO USUARIO":
                # CASO "0" - SAIR:
                if escolha_usuario3 == 0:
                    repetir3 = 2


                # CASO "1" - ACERTAR O TEMPO E INICIAR CONTAGEM:
                if escolha_usuario3 == 1:
                                                                    
                    print("\n")
                    print("	DEFINIR TEMPO:")
            
                    # SEGUNDOS:
                    while tempo_aux1 < 1:
                        
                        print("\n	SEGUNDOS:")
                        tempo6 = int(input("	DIGITE OS SEGUNDOS PARTE 1 - ( 0 - 9 ): "))
                        tempo5 = int(input("	DIGITE OS SEGUNDOS PARTE 2 - ( 0 - 5 ): "))
                                                                        
                        if tempo6 < 10 and tempo5 < 6:
                            tempo_aux1 = 1
                                                                    
                    # MINUTOS:
                    while tempo_aux2 < 1:
                        
                        print("\n	MINUTOS:")			            
                        tempo4 = int(input("	DIGITE OS MINUTOS PARTE 1 - ( 0 - 9 ): "))
                        tempo3 = int(input("	DIGITE OS MINUTOS PARTE 2 - ( 0 - 5 ): "))

                        if tempo4 < 10 and tempo3 < 6:
                            tempo_aux2 = 1
                                                                    
                    # HORAS:
                    while tempo_aux3 < 1:
                        
                        print("\n	HORAS:")
                        tempo2 = int(input("	DIGITE AS HORAS PARTE 1 - ( 0 - 9 ): "))
                            
                        if tempo2 < 10:
                            tempo_aux3 = 1


                    print("\n")
                    aux1 = 0
                    aux2 = 1
                    print("	CONTAGEM:")	
                                                                    
                    while aux2 < 3:			        	
                        print("	TEMPORIZADOR - ", tempo2, "h", tempo3, tempo4, "m", tempo5, tempo6, "s")
                        tempo6 = tempo6 - 1

                        # SEGUNDOS:
                        if tempo6 < 0:
                            tempo6 = 9
                            tempo5 = tempo5 - 1
                        
                        if tempo5 < 0:
                            tempo5 = 5
                            tempo4 = tempo4 - 1
                                                
                        # MINUTOS:
                        if tempo4 < 0:
                            tempo4 = 9
                            tempo3 = tempo3 - 1
                        
                        if tempo3 < 0:
                            tempo3 = 5
                            tempo2 = tempo2 - 1
                                                
                        # HORAS:
                        if tempo2 == 0 and tempo3 == 0 and tempo4 == 0 and tempo5 == 0 and tempo6 == 0:
                                                                    
                            tempo2 = 1
                            tempo3 = 0
                            tempo4 = 0
                            tempo5 = 5
                            tempo6 = 9
                            break
                                                                        
                        time.sleep(1.0)
                                        
                            
                # "EM CASO DE VALORES INVALIDOS":
                if escolha_usuario3 != 0 and escolha_usuario3 != 1:

                    print("\n        POR FAVOR DIGITE UM VALOR VALIDO!")
                    print("        TENTE NOVAMENTE!")
                            
                        
        # "EM CASO DE VALORES INVALIDOS":
        if escolha_usuario != 0 and escolha_usuario != 1 and escolha_usuario != 2:

                    print("\n        POR FAVOR DIGITE UM VALOR VALIDO!")
                    print("        TENTE NOVAMENTE!")

    except Exception:

        print("\n        ERRO!")
        print("        POR FAVOR TENTE NOVAMENTE!")




        
