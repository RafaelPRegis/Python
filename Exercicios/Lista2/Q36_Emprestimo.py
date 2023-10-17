"""
EXERCÍCIO 036: Aprovando Empréstimo

Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário, ou então o empréstimo será negado.
"""

from time import sleep


#Inicialização
print()
mensagem = "Calculadora de Emprestimo"

for i in range (2):
    for caractere in mensagem:
        print(caractere, end='', flush=True)
        sleep(0.1)
    print()

sleep(1)


#Entrada de Variaveis
print()
print('-=-' * 20, "\n")
print("Preencha as seguintes informações")
print()

casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))


#Calculo
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100


#Print
print('Para pagar uma casa de R$ {:.2f} em {} anos,'.format(casa, anos), end=' ')
print('a prestação será de R$ {:.2f}.'.format(prestacao))
if prestacao <= minimo:
    print('Empréstimo poderá ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
