

	# [" CRIADOR: LUIZ ÂNGELO MARTINS "]:

	# DESCRIÇÃO:
            #PROGRAMA SIMPLES PARA GERAR NÚMEROS ALEATÓRIOS.

	# COMPILADOR / IDE USADO(A):
            # IDLE PYTHON	


# IMPORTAÇÃO DE BIBLIOTECAS::
import time
from random import randint
#time.sleep(0.3)
#print(len(vetor_numero))


# DECLARAÇÃO DE VARIAVEIS "INTEIRAS":
aux1 = 0
valor1 = 0
valor2 = 0
escolha = 0
repetir = 1
aux0 = 0
repetidor1 = 0
repetidor2 = 0

while repetir != 0:
    
    try:
        
        # "ZERANDO VALORES":   
        aux1 = 0
        valor1 = 0
        valor2 = 0
        escolha = 0
        repetir = 1
        repetidor1 = 0
        repetidor2 = 0
                
        # EXIBIÇÃO/CONSTRUÇÃO DO MENU:
        aux1 = 0
        print("\n")
        print("	GERADOR DE NUMEROS ALEATORIOS:\n")    
        print("	0 - SAIR.")
        print("	1 - GERAR NUMERO(S) ALEATORIO(S).\n")
        escolha = int(input("	DIGITE SUA RESPOSTA: "))
       
        # "FILTRAGEM DA ESCOLHA DO USUARIO":
        # CASO "0" - SAIR:
        if escolha ==  0:
            exit()
        
        # CASO "1" - GERAR NÚMERO(S) ALEATÓRIO(S):
        if escolha == 1:
                        
            while aux1 < 1:
                            
                print("\n\n	ENTRADA DE DADOS:")
                valor1 = int(input("\n	DESEJA GERAR QUANTOS NUMEROS ?: 1 - 9: "))
                valor2 = int(input("	DESEJA GERAR NUMEROS ENTRE QUAL INTERVALO ?: 1 - "))
                vetor_numero = [0]*valor1
                                                    
                if valor1 < 10:
                                                            
                    aux1 = 1
                                                            
                    # GERANDO O VETOR:
                    while repetidor1 < valor1:

                        vetor_numero[repetidor1] = (randint(1,valor2))
                        repetidor1 = repetidor1 + 1

                    print("\n	QUANTIA - ", valor1)
                    print("	INTERVALO - ", valor2, "\n")
                    
                    # ORDENANDO O VETOR:
                    vetor_numero_aux = [0]*valor1
                    vetor_numero_aux = sorted(vetor_numero)
                     
                    # EXIBINDO OS VALORES:
                    while repetidor2 != valor1:
                                                                    
                        print("	ALEATORIO ", repetidor2 + 1, " - ", vetor_numero_aux[repetidor2] )
                        repetidor2 = repetidor2 + 1
                        
                    print("\n	NUMEROS GERADOS COM SUCESSO!")
                    
        # "EM CASO DE VALORES INVALIDOS":
        if escolha != 0 and escolha != 1:

            print("\n        POR FAVOR DIGITE UM VALOR VALIDO!")
            print("        TENTE NOVAMENTE!")
        
    except Exception:

        print("\n        ERRO!")
        print("        POR FAVOR TENTE NOVAMENTE!")




