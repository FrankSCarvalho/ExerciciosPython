# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
import sys
sys.path.append('/home/frank/Documentos/GitHub/ExerciciosPython')

from testaInput import *

print('Calcular o dobro da área de um quadrado')

while True:
    lado = input('Digite o valor do lado do quadrado: ')

    resposta = testaInput(lado)

    if resposta == 'letra':
        print('Digite apenas numeros para continuar. Tente novamente!')
    elif resposta == 'vazio':
        print('Digite apenas numeros para continuar. Tente novamente!')
    else:
        area = float(lado) * 4
        dobro = area * 2
    
        print(f'O dobro da área do quareado é: {dobro}')
        break

    break

