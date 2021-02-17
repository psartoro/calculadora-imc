print('====CALCULADORA IMC====')
nome = bool(input('Insira seu nome: '))


# Funcao
# Se um dos valores for igual a vazio, retorna 0
def calculaimc(pes, alt):
    if pes != '' and alt != '':
        pes = float(pes)
        alt = float(alt)
        imc = pes / (alt * alt)
        return imc
    else:
        return 0


if nome == False:
    print('Fim... valores inseridos inválidos!!!')
else:
    peso = input('Insira seu peso: ')
    altura = input('Insira sua altura: ')
    # Chamada da Funcao
    imc = calculaimc(peso, altura)
    if imc > 0:
        if imc < 18.5:
            print('Seu IMC é de:', round(imc))
            print('Cuidado {}!!! Você está abaixo do peso!'.format(nome))
        elif 18.5 <= imc <= 24.9:
            print('Seu IMC é de:', round(imc))
            print('Parabéns {}!!! Seu peso está normal!'.format(nome))
        elif 25.0 <= imc <= 29.9:
            print('Seu IMC é:', round(imc))
            print('Cuidado {}!!! Você está acima de seu peso!'.format(nome))
        elif 30.0 <= imc <= 34.9:
            print('Seu IMC é:', round(imc))
            print('Atenção {}!!! Obesidade grau I'.format(nome))
        elif imc >= 35.0:
            print('Seu IMC é:', round(imc))
            print('Atenção {}!!! Obesidade grau II'.format(nome))
        else:
            print('Seu IMC é:', round(imc))
            print('Atenção {}!!! Obesidade grau III'.format(nome))
    else:
        print('Fim... valores inseridos inválidos!!!')
