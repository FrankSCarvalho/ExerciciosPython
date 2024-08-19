#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
from testaInput import testaInput

print('Calcular a área de um circula')

while True:
    raio = input('Digite o raio do círculo: ')

    resposta = testaInput(raio)

    if resposta == 'letra':
        print('Digite apenas numeros para continuar. Tente novamente!')
    elif resposta == 'vazio':
        print('Digite apenas numeros para continuar. Tente novamente!')
    else:
        raio = float(raio)
        pi = 3.14
        area = pi*raio**2
        print(f'A area do circulo com o raio {raio} é = {area}')
        break
