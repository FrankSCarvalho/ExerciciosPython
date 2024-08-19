# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

print('Calculadora de médias escolares bimestrais')


def testarNotas(bim, nota):
    controle = ''
    if nota.isalpha():
        controle = 'letra'        
        return controle
    elif float(nota) < 0 or float(nota) > 10:
        controle = 'estouro'
        return controle
    else:
        nota = float(nota)
        return nota



while True:
    n1 = input('Digite a Nota do 1° Bimestre: ')
    resultado = testarNotas(1,n1)

    if resultado == 'letra':
        print('Voçe não pode digitar Letras. Tente novamente!')
    elif resultado == 'estouro':
        print('A nota deve estar entre 0 e 10. Tente novamente!')
    else:
        b1 = resultado
        break

while True:
    n2 = input('Digite a Nota do 2° Bimestre: ')
    resultado = testarNotas(2,n2)

    if resultado == 'letra':
        print('Voçe não pode digitar Letras. Tente novamente!')
    elif resultado == 'estouro':
        print('A nota deve estar entre 0 e 10. Tente novamente!')
    else:
        b2 = resultado
        break

while True:
    n3 = input('Digite a Nota do 3° Bimestre: ')
    resultado = testarNotas(3,n3)

    if resultado == 'letra':
        print('Voçe não pode digitar Letras. Tente novamente!')
    elif resultado == 'estouro':
        print('A nota deve estar entre 0 e 10. Tente novamente!')
    else:
        b3 = resultado
        break

while True:
    n4 = input('Digite a Nota do 4° Bimestre: ')
    resultado = testarNotas(4,n4)

    if resultado == 'letra':
        print('Voçe não pode digitar Letras. Tente novamente!')
    elif resultado == 'estouro':
        print('A nota deve estar entre 0 e 10. Tente novamente!')
    else:
        b4 = resultado
        break

media = (b1+b2+b3+b4)/4
print(f'A média do aluno é: {media}')
print('A média para aprovação é de 8.0')

if media < 8:
    print('O aluno não alcançou a média. Resultado: REPROVADO')
elif media ==8:
    print('O aluno está na média. Resultado: APROVADO')
else:
    print('Aluno acima da média. Resultado: APROVADO')