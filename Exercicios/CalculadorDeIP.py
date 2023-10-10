"""
Programa com o objetivo de receber um IP e fazer os calculos de variação.

"""
from time import sleep


#Inicialização
print()
mensagem = "Iniciando... ... ... ... ... ..."

for i in range (2):
    for caractere in mensagem:
        print(caractere, end='', flush=True)
        sleep(0.1)
    print()

sleep(1)


while True:
    
    print()
    print('-=-' * 20, "\n")
    
    #IP e Mascara
    IP = str(input('Digite o IP para o calculo: ')).split(".")
    Masc = int(input('Agora digite a mascara: '))

    print()
    print('-=-' * 20)

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
    VariB = Variação
    

    #Variação Grande
    if Variação > 256:
        Variação = Variação / 256


    #Print da Tabela
    for i in range(1, SubRede):
        cunclu = Variação - VariB
        print(f"{IP[:2]}.{cunclu}.0 | {IP[:3]}.1 -- {IP[:2]}.{Variação - 1}.254 | {IP[:2]}.{Variação - 1}.255")
        Variação += VariB
    

    #Confirmação para o Loop Da calculadora
    if str(input("Deseja calcular novamente? ")).upper() == "N":
        break
    
    #Reiniciando
    for i in range (3):
        print("Reiniciando ... ...")
        sleep(1)
    
    print("\n", '-=-' * 20)