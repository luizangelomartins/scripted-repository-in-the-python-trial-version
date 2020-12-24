


    # [" CRIADOR: LUIZ ÂNGELO MARTINS "]:

    # DESCRIÇÃO:
    # PROJETO DE CALCULOS QUE CONSISTE EM:		
    # DIVISÃO,
    # MULTIPLICAÇÃO,
    # POTÊNCIAÇÃO,
    # RADICIAÇÃO,
    # SOMA,
    # SUBTRAÇÃO.

    # COMPILADOR USADO:
    # IDLE PYTHON	


# IMPORTAÇÃO DE BIBLIOTECAS::
import math


# DECLARAÇÃO DE VARIAVEIS:
repetir = 1
escolha_usuario = 0
repetir_conta = 1
escolha_conta = 0
val1 = 0
val2 = 0
        
while repetir > 0:

    try:
        
        repetir = 1
        escolha_usuario = 0
        repetir_conta = 1
        escolha_conta = 0
        val1 = 0
        val2 = 0
        
        # EXIBIÇÃO DO MENU: 
        print("\n")    
        print("	CALCULADORA SIMPLES:")
        print("	MENU PRINCIPAL \n");
        print("	0 - SAIR.")
        print("	1 - SOMAR.")
        print("	2 - SUBTRAIR.")
        print("	3 - MULTIPLICAR.")
        print("	4 - DIVIDIR.")
        print("	5 - RAIZ QUADRADA.")
        print("	6 - POTENCIACAO. ")
        print("")    
        escolha_usuario = int(input("	DIGITE SUA RESPOSTA: "))

        # CASO "0" - SAIR:
        if escolha_usuario == 0:
            exit()
         
        # CASO "1" - SOMAR:
        if escolha_usuario == 1:
            
            repetir_conta = 1
            val1 = 0
            val2 = 0

            while repetir_conta > 0:
                 
                print("\n")
                print("	MENU - SOMAR: \n")
                print("	0 - VOLTAR AO MENU PRINCIPAL.")
                print("	1 - ADICIONAR VALOR INICIAL.")
                print("	2 - SOMAR VALORES.")
                print("		| TOTAL DA SOMA: ", val2)
                print("\n")
                escolha_conta = int(input("	DIGITE SUA RESPOSTA: "))

                # CASO "0" - VOLTAR AO MENU PRINCIPAL:
                if escolha_conta == 0:
                       
                    val1 = 0
                    val2 = 0
                    repetir_conta = 0

                # CASO "1" - ADICIONAR VALOR INICIAL:
                if escolha_conta == 1:
		
                    val2 = float(input("	DIGITE O VALOR INICIAL PARA SOMA: "))

                # CASO "2" - ADICIONAR VALORES | [ SOMAR ]: 
                if escolha_conta == 2:

                    val1 = float(input("	DIGITE O VALOR PARA ADICAO: "))
                    val2 = val2 + val1
                    val2 = round(val2,2)

                # VALORES INVALIDOS:
                if escolha_conta != 0 and escolha_conta != 1 and escolha_conta != 2:
       
                    print("\n")
                    print("	VALOR INVALIDO!")
                    print("	POR FAVOR TENTE NOVAMENTE!")

        # CASO "2" - SUBTRAIR:
        if escolha_usuario == 2:
            
            repetir_conta = 1
            val1 = 0
            val2 = 0

            while repetir_conta > 0:
                 
                print("\n")
                print("	MENU - SUBTRAIR: \n")
                print("	0 - VOLTAR AO MENU PRINCIPAL.")
                print("	1 - ADICIONAR VALOR INICIAL.")
                print("	2 - SUBTRAIR VALORES.")
                print("		| TOTAL DA SUBTRACAO: ", val2)
                print("\n")
                escolha_conta = int(input("	DIGITE SUA RESPOSTA: "))

                # CASO "0" - VOLTAR AO MENU PRINCIPAL:
                if escolha_conta == 0:
                       
                    val1 = 0
                    val2 = 0
                    repetir_conta = 0

                # CASO "1" - ADICIONAR VALOR INICIAL:
                if escolha_conta == 1:
		
                    val2 = float(input("	DIGITE O VALOR INICIAL PARA SUBTRACAO: "))

                # CASO "2" - ADICIONAR VALORES | [ SUBTRACAO ]: 
                if escolha_conta == 2:

                    val1 = float(input("	DIGITE O VALOR PARA SUBTRACAO: "))
                    val2 = val2 - val1
                    val2 = round(val2,2)

                # VALORES INVALIDOS:
                if escolha_conta != 0 and escolha_conta != 1 and escolha_conta != 2:
       
                    print("\n")
                    print("	VALOR INVALIDO!")
                    print("	POR FAVOR TENTE NOVAMENTE!")

        # CASO "3" - MULTIPLICAR:
        if escolha_usuario == 3:
            
            repetir_conta = 1
            val1 = 0
            val2 = 0

            while repetir_conta > 0:
                 
                print("\n")
                print("	MENU - MULTIPLICAR: \n")
                print("	0 - VOLTAR AO MENU PRINCIPAL.")
                print("	1 - ADICIONAR VALOR INICIAL.")
                print("	2 - MULTIPLICAR VALORES.")
                print("		| TOTAL DA MULTIPLICACAO: ", val2)
                print("\n")
                escolha_conta = int(input("	DIGITE SUA RESPOSTA: "))

                # CASO "0" - VOLTAR AO MENU PRINCIPAL:
                if escolha_conta == 0:
                       
                    val1 = 0
                    val2 = 0
                    repetir_conta = 0

                # CASO "1" - ADICIONAR VALOR INICIAL:
                if escolha_conta == 1:
		
                    val2 = float(input("	DIGITE O VALOR INICIAL PARA MULTIPLICACAO: "))

                # CASO "2" - ADICIONAR VALORES | [ MULTIPLICACAO ]: 
                if escolha_conta == 2:

                    val1 = float(input("	DIGITE O VALOR PARA MULTIPLICACAO: "))
                    val2 = val2 * val1
                    val2 = round(val2,2)

                # VALORES INVALIDOS:
                if escolha_conta != 0 and escolha_conta != 1 and escolha_conta != 2:
       
                    print("\n")
                    print("	VALOR INVALIDO!")
                    print("	POR FAVOR TENTE NOVAMENTE!")

        # CASO "4" - DIVIDIR:
        if escolha_usuario == 4:
            
            repetir_conta = 1
            val1 = 0
            val2 = 0

            while repetir_conta > 0:
                 
                print("\n")
                print("	MENU - DIVIDIR: \n")
                print("	0 - VOLTAR AO MENU PRINCIPAL.")
                print("	1 - ADICIONAR VALOR INICIAL.")
                print("	2 - DIVIDIR VALORES.")
                print("		| TOTAL DA DIVISAO: ", val2)
                print("\n")
                escolha_conta = int(input("	DIGITE SUA RESPOSTA: "))

                # CASO "0" - VOLTAR AO MENU PRINCIPAL:
                if escolha_conta == 0:
                       
                    val1 = 0
                    val2 = 0
                    repetir_conta = 0

                # CASO "1" - ADICIONAR VALOR INICIAL:
                if escolha_conta == 1:
		
                    val2 = float(input("	DIGITE O VALOR INICIAL PARA DIVISAO: "))

                # CASO "2" - ADICIONAR VALORES | [ DIVISAO ]: 
                if escolha_conta == 2:

                    val1 = float(input("	DIGITE O VALOR PARA DIVISAO: "))
                    val2 = val2 / val1
                    val2 = round(val2,2)

                # VALORES INVALIDOS:
                if escolha_conta != 0 and escolha_conta != 1 and escolha_conta != 2:
       
                    print("\n")
                    print("	VALOR INVALIDO!")
                    print("	POR FAVOR TENTE NOVAMENTE!")

        # CASO "5" - RAIZ QUADRADA:
        if escolha_usuario == 5:
            
            repetir_conta = 1
            val1 = 0
            val2 = 0

            while repetir_conta > 0:
                 
                print("\n")
                print("	MENU - RAIZ QUADRADA: \n")
                print("	0 - VOLTAR AO MENU PRINCIPAL.")
                print("	1 - ADICIONAR VALOR INICIAL.")
                print("	2 - CALCULAR RAIZ.")
                print("		| TOTAL DA RADICIACAO: ", val2)
                print("\n")
                escolha_conta = int(input("	DIGITE SUA RESPOSTA: "))

                # CASO "0" - VOLTAR AO MENU PRINCIPAL:
                if escolha_conta == 0:
                       
                    val1 = 0
                    val2 = 0
                    repetir_conta = 0

                # CASO "1" - ADICIONAR VALOR INICIAL:
                if escolha_conta == 1:
		
                    val2 = float(input("	DIGITE O VALOR INICIAL PARA O CALCULO DA RAIZ: "))

                # CASO "2" - ADICIONAR VALORES | [ RADICIACAO ]: 
                if escolha_conta == 2:

                    val2 = math.sqrt(val2)
                    val2 = round(val2,2)

                # VALORES INVALIDOS:
                if escolha_conta != 0 and escolha_conta != 1 and escolha_conta != 2:
       
                    print("\n")
                    print("	VALOR INVALIDO!")
                    print("	POR FAVOR TENTE NOVAMENTE!")

        # CASO "6" - POTENCIACAO:
        if escolha_usuario == 6:
            
            repetir_conta = 1
            val1 = 0
            val2 = 0

            while repetir_conta > 0:
                 
                print("\n")
                print("	MENU - POTENCIACAO: \n")
                print("	0 - VOLTAR AO MENU PRINCIPAL.")
                print("	1 - ADICIONAR VALOR INICIAL.")
                print("	2 - CALCULAR POTENCIA.")
                print("		| TOTAL DA POTENCIACAO: ", val2)
                print("\n")
                escolha_conta = int(input("	DIGITE SUA RESPOSTA: "))

                # CASO "0" - VOLTAR AO MENU PRINCIPAL:
                if escolha_conta == 0:
                       
                    val1 = 0
                    val2 = 0
                    repetir_conta = 0

                # CASO "1" - ADICIONAR VALOR INICIAL:
                if escolha_conta == 1:
		
                    val2 = float(input("	DIGITE O VALOR INICIAL PARA O CALCULO DA POTENCIA: "))

                # CASO "2" - ADICIONAR VALORES | [ POTENCIACAO ]: 
                if escolha_conta == 2:

                    val1 = float(input("	DIGITE O VALOR DO EXPOENTE: "))
                    val2 = (val2 ** val1)
                    val2 = round(val2,2)

                # VALORES INVALIDOS:
                if escolha_conta != 0 and escolha_conta != 1 and escolha_conta != 2:
       
                    print("\n")
                    print("	VALOR INVALIDO!")
                    print("	POR FAVOR TENTE NOVAMENTE!")
                    
        # VALORES INVALIDOS:
        if escolha_usuario != 0 and escolha_usuario != 1 and escolha_usuario != 2 and escolha_usuario != 3 and escolha_usuario != 4 and escolha_usuario != 5 and escolha_usuario != 6:

            print("\n")
            print("	VALOR INVALIDO!")
            print("	POR FAVOR TENTE NOVAMENTE!")
                    
    except Exception:

        print("\n        ERRO!")
        print("        POR FAVOR TENTE NOVAMENTE!")


