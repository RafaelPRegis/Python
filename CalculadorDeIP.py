"""
Programa com o objetivo de receber um IP e fazer os calculos de variação.

"""
from time import sleep



while True:

    #IP e Mascara
    IP = str(input('Digite o IP para o calculo: '))
    Masc = int(input('Agora digite a mascara: '))

    print('\n', '-=-' * 20)

    #Subrede e Hosts
    SubRede = int(input('\nQual a subrede necessaria? '))
    Hosts = int(input('E quantos hosts são necessarios? '))
    SB = int(2)
    Bits = int(1)

    #Calculo para Bits
    while SB < SubRede:
        SB = SB ** Bits
        Bits += 1
    

    #Mascara Nova e Variação
    Masc += Bits
    Variação = 2 ** (32 - Masc)

    #Variação Grande
    if Variação > 256:
        Variação = Variação / 256

    #Print da Tabela
    for i in range(1, SubRede):
        print(IP, SubRede, Bits, Variação, Masc)
    

    #Confirmação para o Loop Da calculadora
    if str(input("Deseja calcular novamente? ")).upper() == "N":
        break
    
    #Reiniciando
    for i in range (3):
        print("Reiniciando ... ...")
        sleep(1)
    
    print("\n", '-=-' * 20)