# Faça um Programa que converta metros para centímetros.

print('Converssão de metros para centimetros')

def conversor(metros):
        controle = 0
        if metros.isalpha():
            controle = 'letra'
            return controle
        elif metros == '':
            controle = 'vazio'
            return controle
        else:
            centimetros = float(metros)* 100
            return centimetros

while True:

    metros = input('Digite a quantidade de metros: ')
    
    resposta = conversor(metros)

    if resposta == 'letra':
        print('Digite apenas números para calcular. Tente mais uma vez!')
    elif resposta == 'vazio':
        print('Não pode deixar a resposta vazia digite um número para continuar')
    else:
        print(f'{metros} metros é equivalente a {resposta} centimetros.')
        break

    