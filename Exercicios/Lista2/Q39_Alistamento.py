"""
EXERCÍCIO 039: Alistamento Militar

Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar, ou se já passou
do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

date = Variavel do tipo tempo, como dias, meses e anos
"""

from datetime import date



#Informações
atual = date.today().year
name = str(input("Qual seu nome? "))
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc

#Saida de Infos
print('Olá {} você nasceu em {} tem {} anos em {}.'.format(name, nasc, idade, atual))

#Informação sobre Alistamento
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento.'.format(saldo))
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    print('Seu alistamento foi em {}.'.format(ano))