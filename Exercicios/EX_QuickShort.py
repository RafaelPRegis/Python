"""
Programa que utiliza do QuickShort para ordenar uma lista

---> Eplicação de ferramentas <----
>QuickShort = Criação de uma função para encurtar e almentar a eficacia da leitura de listas,
            dividindo a lista.

>len = Ler o tamanho da lista

"""


#Criação da Função
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    #Ordenação da lista
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


#Exemplo de uso:
    #Preenchimento da função / Substitui o arr
    lista = [3, 6, 8, 10, 1, 2, 1]
    resultado = quicksort(lista)

    #Print
    print(resultado)
