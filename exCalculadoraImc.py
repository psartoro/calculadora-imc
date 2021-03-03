print('{:-^25}\n'.format('CALCULADORA IMC'))
nome = ""
peso = ""
altura = ""

while True:
    nome = input('Digite seu nome: ').strip()
    peso = input('Digite seu peso: ').strip()
    altura = input('Digite sua altura: ').strip()
    dados = [nome, peso, altura]
    if '0' in dados or '' in dados:
        print('Valores incorretos!')
    else:
        break

calc = lambda x, y: x / (y ** 2)
imc = calc(float(dados[1]), float(dados[2]))

print('-' * 45)

if imc < 18.5:
    print('Seu IMC é de:', round(imc))
    print('\033[1;33mCuidado {}!!!\033[m Você está abaixo do peso!'.format(nome.capitalize()))
elif 18.5 <= imc <= 24.9:
    print('Seu IMC é de:', round(imc))
    print('\033[1;32mParabéns {}!!!\033[m Seu peso está normal!'.format(nome.capitalize()))
elif 25.0 <= imc <= 29.9:
    print('Seu IMC é:', round(imc))
    print('\033[1;33mCuidado {}!!!\033[m Você está acima de seu peso!'.format(nome.capitalize()))
elif 30.0 <= imc <= 34.9:
    print('Seu IMC é:', round(imc))
    print('\033[1;31mAtenção {}!!!\033[m Obesidade grau I'.format(nome.capitalize()))
elif 35 <= imc <= 39.9:
    print('Seu IMC é:', round(imc))
    print('\033[1;31mAtenção {}!!!\033[m Obesidade grau II'.format(nome.capitalize()))
elif 40 <= imc:
    print('Seu IMC é:', round(imc))
    print('\033[1;31mAtenção {}!!!\033[m Obesidade grau III'.format(nome.capitalize()))

print('-' * 45)
