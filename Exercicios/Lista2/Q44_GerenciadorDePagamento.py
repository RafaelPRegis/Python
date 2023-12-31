"""
EXERCÍCIO 044: Gerenciador de Pagamentos

Elabore um programa que calcule o valor a ser pago de um produto,
considerando o seu preço normal, e condição de pagamento:

- À vista no dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""


#Valor do Produto
print('{:=^40}'.format(' LOJAS GUANABARA '))
preco = float(input('Preço das compras: R$ '))

#Forma de Pagamento
print('''FORMAS DE PAGAMENTO
[ 1 ] À vista no dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))

#Calculos de Pagamento
#Cheque
if opcao == 1:
    total = preco - (preco * 10 / 100)

#À Vista
elif opcao == 2:
    total = preco - (preco * 5 / 100)

#Parcelado em 2 vezes
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f} SEM JUROS.'.format(parcela))

#Parcelado em 3 vezes
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS.'.format(totparc, parcela))

#Erro
else:
    total = preco
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')

#Print Final
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(preco, total))