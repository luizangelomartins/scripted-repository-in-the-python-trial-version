


    # [" CRIADOR: LUIZ ÂNGELO MARTINS "]:

    # DESCRIÇÃO:
    # PROGRAMA QUE VISA CONVERTER OS VALORES DAS PRINCIPAIS MOEDAS DO MUNDO:
    # - Real,
    # - Dólar Americano,
    # - Dólar Australiano,
    # - Dólar Canadense,
    # - Euro,
    # - Franco Suíço,
    # - Iene,
    # - Libra esterlina,
    # - Lira Turca,
    # - Peso Argentino,
    # - Renmimbi.
	
    # COMPILADOR USADO:
    # IDLE PYTHON
		

# IMPORTAÇÃO DE BIBLIOTECAS::
import math

	
# DECLARAÇÃO DE VARIAVEIS:
repetir = 0
escolha1 = 0
nome = ""
valor_moeda = 0.0
quantia_moeda = 0.0
resultado = 0.0
	
while repetir < 1:

    try:
    
        nome = ""
        print("")  
        print("	MENU GERAL - CONVERSOR:")
        print("")
        print("	0 - SAIR.")
        print("	1 - REAL.")
        print("	2 - EURO.")
        print("	3 - IENE.")
        print("	4 - DOLAR AMERICANO.")
        print("	5 - DOLAR AUSTRALIANO.")
        print("	6 - DOLAR CANADENSE.")
        print("	7 - FRANCO SUICO.")
        print("	8 - LIBRA ESTERLINA.")
        print("	9 - LIRA TURCA.")
        print("	10 - PESO ARGENTINO.")
        print("	11 - RENMIMBI.")
        print("")
        escolha1 = int(input("	DIGITE SUA RESPOSTA: "))

        # CASO "0" - SAIR:
        if escolha1 == 0:
            exit()
            
        # CASO "1" - REAL:
        if escolha1 == 1:
            nome = "REAL"
            print("")
            print("	MENU GERAL - ", nome)
            print("")
            print("	DIGITE O VALOR UNITARIO ATUAL DE(A)", nome, "(S) EM RELACAO A MOEDA DE INTERESSE:")
            valor_moeda = float(input("	DIGITE O VALOR: "))
            print("")
            print("	DIGITE A QUANTIA DE(A)", nome, "(S) EM POSSE:")
            quantia_moeda = float(input("	DIGITE A QUANTIA: "))
            resultado = valor_moeda * quantia_moeda
            resultado = round(resultado,2)
            print("")
            print("	VOCE TEM:", resultado, "DA MOEDA INTERESSADA EM POSSE.")

        # CASO "2" - EURO:
        if escolha1 == 2:
            nome = "EURO"
            print("")
            print("	MENU GERAL - ", nome)
            print("")
            print("	DIGITE O VALOR UNITARIO ATUAL DE(A)", nome, "(S) EM RELACAO A MOEDA DE INTERESSE:")
            valor_moeda = float(input("	DIGITE O VALOR: "))
            print("")
            print("	DIGITE A QUANTIA DE(A)", nome, "(S) EM POSSE:")
            quantia_moeda = float(input("	DIGITE A QUANTIA: "))
            resultado = valor_moeda * quantia_moeda
            resultado = round(resultado,2)
            print("")
            print("	VOCE TEM:", resultado, "DA MOEDA INTERESSADA EM POSSE.")

        # CASO "3" - IENE:
        if escolha1 == 3:
            nome = "IENE"
            print("")
            print("	MENU GERAL - ", nome)
            print("")
            print("	DIGITE O VALOR UNITARIO ATUAL DE(A)", nome, "(S) EM RELACAO A MOEDA DE INTERESSE:")
            valor_moeda = float(input("	DIGITE O VALOR: "))
            print("")
            print("	DIGITE A QUANTIA DE(A)", nome, "(S) EM POSSE:")
            quantia_moeda = float(input("	DIGITE A QUANTIA: "))
            resultado = valor_moeda * quantia_moeda
            resultado = round(resultado,2)
            print("")
            print("	VOCE TEM:", resultado, "DA MOEDA INTERESSADA EM POSSE.")

        # CASO "4" - DOLAR AMERICANO:
        if escolha1 == 4:
            nome = "DOLAR AMERICANO"
            print("")
            print("	MENU GERAL - ", nome)
            print("")
            print("	DIGITE O VALOR UNITARIO ATUAL DE(A)", nome, "(S) EM RELACAO A MOEDA DE INTERESSE:")
            valor_moeda = float(input("	DIGITE O VALOR: "))
            print("")
            print("	DIGITE A QUANTIA DE(A)", nome, "(S) EM POSSE:")
            quantia_moeda = float(input("	DIGITE A QUANTIA: "))
            resultado = valor_moeda * quantia_moeda
            resultado = round(resultado,2)
            print("")
            print("	VOCE TEM:", resultado, "DA MOEDA INTERESSADA EM POSSE.")

        # CASO "5" - DOLAR AUSTRALIANO:
        if escolha1 == 5:
            nome = "DOLAR AUSTRALIANO"
            print("")
            print("	MENU GERAL - ", nome)
            print("")
            print("	DIGITE O VALOR UNITARIO ATUAL DE(A)", nome, "(S) EM RELACAO A MOEDA DE INTERESSE:")
            valor_moeda = float(input("	DIGITE O VALOR: "))
            print("")
            print("	DIGITE A QUANTIA DE(A)", nome, "(S) EM POSSE:")
            quantia_moeda = float(input("	DIGITE A QUANTIA: "))
            resultado = valor_moeda * quantia_moeda
            resultado = round(resultado,2)
            print("")
            print("	VOCE TEM:", resultado, "DA MOEDA INTERESSADA EM POSSE.")

        # CASO "6" - DOLAR AUSTRALIANO:
        if escolha1 == 6:
            nome = "DOLAR CANADENSE"
            print("")
            print("	MENU GERAL - ", nome)
            print("")
            print("	DIGITE O VALOR UNITARIO ATUAL DE(A)", nome, "(S) EM RELACAO A MOEDA DE INTERESSE:")
            valor_moeda = float(input("	DIGITE O VALOR: "))
            print("")
            print("	DIGITE A QUANTIA DE(A)", nome, "(S) EM POSSE:")
            quantia_moeda = float(input("	DIGITE A QUANTIA: "))
            resultado = valor_moeda * quantia_moeda
            resultado = round(resultado,2)
            print("")
            print("	VOCE TEM:", resultado, "DA MOEDA INTERESSADA EM POSSE.")

        # CASO "7" - FRANCO SUICO:
        if escolha1 == 7:
            nome = "FRANCO SUICO"
            print("")
            print("	MENU GERAL - ", nome)
            print("")
            print("	DIGITE O VALOR UNITARIO ATUAL DE(A)", nome, "(S) EM RELACAO A MOEDA DE INTERESSE:")
            valor_moeda = float(input("	DIGITE O VALOR: "))
            print("")
            print("	DIGITE A QUANTIA DE(A)", nome, "(S) EM POSSE:")
            quantia_moeda = float(input("	DIGITE A QUANTIA: "))
            resultado = valor_moeda * quantia_moeda
            resultado = round(resultado,2)
            print("")
            print("	VOCE TEM:", resultado, "DA MOEDA INTERESSADA EM POSSE.")

        # CASO "8" - LIBRA ESTERLINA:
        if escolha1 == 8:
            nome = "LIBRA ESTERLINA"
            print("")
            print("	MENU GERAL - ", nome)
            print("")
            print("	DIGITE O VALOR UNITARIO ATUAL DE(A)", nome, "(S) EM RELACAO A MOEDA DE INTERESSE:")
            valor_moeda = float(input("	DIGITE O VALOR: "))
            print("")
            print("	DIGITE A QUANTIA DE(A)", nome, "(S) EM POSSE:")
            quantia_moeda = float(input("	DIGITE A QUANTIA: "))
            resultado = valor_moeda * quantia_moeda
            resultado = round(resultado,2)
            print("")
            print("	VOCE TEM:", resultado, "DA MOEDA INTERESSADA EM POSSE.")

        # CASO "9" - LIRA TURCA:
        if escolha1 == 9:
            nome = "LIRA TURCA"
            print("")
            print("	MENU GERAL - ", nome)
            print("")
            print("	DIGITE O VALOR UNITARIO ATUAL DE(A)", nome, "(S) EM RELACAO A MOEDA DE INTERESSE:")
            valor_moeda = float(input("	DIGITE O VALOR: "))
            print("")
            print("	DIGITE A QUANTIA DE(A)", nome, "(S) EM POSSE:")
            quantia_moeda = float(input("	DIGITE A QUANTIA: "))
            resultado = valor_moeda * quantia_moeda
            resultado = round(resultado,2)
            print("")
            print("	VOCE TEM:", resultado, "DA MOEDA INTERESSADA EM POSSE.")

        # CASO "10" - PESO ARGENTINO:
        if escolha1 == 10:
            nome = "PESO ARGENTINO"
            print("")
            print("	MENU GERAL - ", nome)
            print("")
            print("	DIGITE O VALOR UNITARIO ATUAL DE(A)", nome, "(S) EM RELACAO A MOEDA DE INTERESSE:")
            valor_moeda = float(input("	DIGITE O VALOR: "))
            print("")
            print("	DIGITE A QUANTIA DE(A)", nome, "(S) EM POSSE:")
            quantia_moeda = float(input("	DIGITE A QUANTIA: "))
            resultado = valor_moeda * quantia_moeda
            resultado = round(resultado,2)
            print("")
            print("	VOCE TEM:", resultado, "DA MOEDA INTERESSADA EM POSSE.")

        # CASO "11" - RENMIMBI:
        if escolha1 == 11:
            nome = "RENMIMBI"
            print("")
            print("	MENU GERAL - ", nome)
            print("")
            print("	DIGITE O VALOR UNITARIO ATUAL DE(A)", nome, "(S) EM RELACAO A MOEDA DE INTERESSE:")
            valor_moeda = float(input("	DIGITE O VALOR: "))
            print("")
            print("	DIGITE A QUANTIA DE(A)", nome, "(S) EM POSSE:")
            quantia_moeda = float(input("	DIGITE A QUANTIA: "))
            resultado = valor_moeda * quantia_moeda
            resultado = round(resultado,2)
            print("")
            print("	VOCE TEM:", resultado, "DA MOEDA INTERESSADA EM POSSE.")

        # VALORES INVALIDOS:
        if escolha1 != 0 and escolha1 != 1 and escolha1 != 2 and escolha1 != 3 and escolha1 != 4 and escolha1 != 5 and escolha1 != 6 and escolha1 != 7 and escolha1 != 8 and escolha1 != 9 and escolha1 != 10 and escolha1 != 11:

            print("")
            print("	VALOR INVALIDO!")
            print("	POR FAVOR TENTE NOVAMENTE!")
                
    except Exception:

        print("\n        ERRO!")
        print("        POR FAVOR TENTE NOVAMENTE!")




