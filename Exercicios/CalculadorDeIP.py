"""
Programa com o objetivo de receber um IP e fazer os calculos de variação.

"""
from time import sleep


#Inicialização
print()
mensagem = "Iniciando... ... ... ... ..."

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
    

    #Variação Grande
    if Variação > 256:
        Variação = Variação / 256
    VariB = Variação


    #Imprime o cabeçalho
    print("{:^25} {:^40} {:^50}".format('END.SubRede', 'END.Hosts', 'BroadCast'))
    print("==="*40)

    #Print da Tabela
    for i in range(1, SubRede):
        cunclu = Variação - VariB

        #Função para imprimir os dados de forma organizada
        def imprimir_tabela(dados):
            for linha in dados:
                print("{:<25} | {:^30} | {:^25}".format(*linha))

        #Informação para imprimir
        dados = [
            ("{}.{}.0".format(IP[:2], cunclu), "{}.1 --- {}.{}.254".format(IP[:3], IP[:2], (Variação - 1)), "{}.{}.255".format(IP[:2], (Variação - 1))),
        ]
        #Print e atualização da Variação
        imprimir_tabela(dados)
        Variação += VariB
    

    #Confirmação para o Loop Da calculadora
    if str(input("Deseja calcular novamente? [Y/N]")).upper() != "Y":
        break
    
    #Reiniciando
    for i in range (3):
        print("Reiniciando ... ...")
        sleep(1)
    
    print("\n", '-=-' * 20)
