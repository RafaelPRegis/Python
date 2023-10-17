"""
init = Serve apenas para iniciar o modulo
Fore = Serve para mudar a cor da letra
Back = Serve para mudar a cor do fundo
"""

from colorama import init, Fore, Back

init()

print(Fore.BLUE + "Opa, eu to azul")
print(Back.RED + "Opa, o clima ta vermelho")
