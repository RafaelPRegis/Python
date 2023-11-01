"""
Programa com o objetivo de receber um IP e fazer os calculos.
Contendo as opções de...
 - Mostrar os calculos feitos
 - Ou de fazer com o minimo de custo

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
    
    #Pergunta para qual opção, minimo de custo ou padrão
    minimumC = str(input("Deseja fazer o calculo do IP com o minimo de Custo? [MC/Padrão]\n")).upper()
    print()

    #IP e Mascara
    IP = str(input('Digite o IP para o calculo: ')).split(".")
    IPsep = [int(ips) for ips in IP]
    MascB = int(input('Agora digite a mascara: '))

    print()
    print('-=-' * 20)

    #Subrede e Hosts
    SubRede = int(input('\nQual a subrede necessaria? '))
    Hosts = int(input('E quantos hosts são necessarios? '))
    Bits = 0
    SB = 1

    #Calculo de Bits
    while SB <= SubRede:
        Bits += 1
        SB = 2 ** Bits
    #!!!!!!!!!!!
    print("Dados: \nSB= {} \nBits= {}".format(SB, Bits))
    print()


    #Nova Mascara
    Masc = MascB + Bits
    #!!!!!!!!!!!
    print("Dados: \nMasc= {}".format(Masc))
    print()


    #Calculo para o Minimo de custo
    if minimumC == "MC":
        variationBase = 0

        while variationBase < Hosts:
            Masc -= 1
            i += 1
            totalMasc = 32 - Masc
            variationBase = 2 ** totalMasc
            '''#!!!!!!!!!!!
            print("Dados: \nMasc Modificada= {} -- {}".format(Masc, i - 1))
            print()
            #!!!!!!!!!!!
            print("Dados: \nTotalMasc= {} \nvariationB= {}".format(totalMasc, variationBase))
            print()'''
    
    #Padrão
    elif minimumC == "PADRÃO":
        totalMasc = 32 - Masc
        variationBase = 2 ** totalMasc

        #!!!!!!!!!!!
        print("Dados: \nTotalMasc= {} \nvariationB= {}".format(totalMasc, variationBase))
        print()
    
    else:
        print("Opção de Calculo invalida, escolha entre [MC/Padrão]")
        break


    #Variação Grande
    if variationBase > 256:
        variation = variationBase / 256
        variation2 = variation
    
    else:
        variation = variationBase
        variation2 = variation


    #Imprime o cabeçalho
    print("{:^25} {:^40} {:^50}".format('END.SubRede', 'END.Hosts', 'BroadCast'))
    print("==="*40)


    #Print da Tabela
    for i in range(0, SubRede):
        cunclu = variation - variation2
        #variation -= 1

        #Função para imprimir os dados de forma organizada
        def imprimir_tabela(dados):
            for linha in dados:
                print("{:<25} | {:^30} | {:^25}".format(*linha))

        #Estrutura da tabela
        if IP[3] == "0":
            dados = [
                ("{}.{:.0f}.0".format('.'.join(IP[:2]), cunclu),
                 "{}.1 --- {}.{:.0f}.254".format('.'.join(IP[:3]), '.'.join(IP[:2]), (variation - 1)),
                 "{}.{:.0f}.255".format('.'.join(IP[:2]), (variation - 1))),
            ]
        
        elif IP[3] != "0":
            dados = [
                ("{}.{:.0f}.0".format('.'.join(IP[:2]), cunclu + IPsep[3]),
                 "{}.{:.0f}.1 --/-- {}.{:.0f}.254".format('.'.join(IP[:2]), cunclu + IPsep[3], '.'.join(IP[:2]), IPsep[3] + variation - 1),
                 "{}.{:.0f}.255".format('.'.join(IP[:2]), IPsep[3] + variation - 1)),
            ]
        
        else:
            print("IP Invalido")
        
        #Print e atualização da Variação
        imprimir_tabela(dados)
        variation += variation2

        #Fim de Loop
        if variation > 255:
            break
    print()
    print()


    #Impressão de Calculos feitos
    print("\n", '-=-' * 20)
    print
    if str(input("Deseja ver todos os calculos feitos? [Y/N]")).upper() == "Y":
        #Espera
        for i in range (3):
            print("Carregando Dados... ...")
            sleep(1)
        print()

        #Bits
        print("Primeiro devemos ver o calculo de Bits")
        print("Fezemos 2 elevado a (X), quando o resultado for maior ou igual a Subrede Necessaria, pegamos o (X)")
        print("--> 2^({}) = {}".format(Bits, SB))
        print()

        #Mascara
        print("Agora, só somar os bits que descobrimos anteriormente com a Mascara")
        print("--> {} + {} = {}".format(MascB, Bits, MascB + Bits))
        print()

        #Variação (Minimo de Custo)
        if minimumC == "MC":
            print("Sendo necessario fazer com o minimo de custo devemos fazer...")
            print("Começamos normal, fazendo 2 elevado a 32-(Mascara)")
            print("Após isso devemos diminuir a mascara até chegar ao numero mais aproximado ao de Hosts Necessario")
            print("--> 2^(32-{}) = {}".format(Masc, variationBase))
            print()
        
        else:
            #Variação (Padrão)
            print("Para se descobrir a variação, deve-se elevar 2 a 32-(Mascara)")
            print("--> 2^(32-{}) = {}".format(Masc, variationBase))
            print()

        #Fim
        print("Com tudo isso é só montar a tabela, a qual se encontra acima")
        print()

    print("\n", '-=-' * 20)
    print()

    #Confirmação para o Loop Da calculadora
    if str(input("Deseja calcular novamente? [Y/N]")).upper() != "Y":
        break
    
    #Reiniciando
    for i in range (3):
        print("Reiniciando ... ...")
        sleep(1)
    
    print("\n", '-=-' * 20)


    
    