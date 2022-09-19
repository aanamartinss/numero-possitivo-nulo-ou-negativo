def numero(num):
    if num > 0:
        print('Positivo')
    elif num == 0:
        print('Nulo')
    else:
        print('Negativo')
num = int(input('informe um número: '))
print('Este número é', ' ')
numero(num)
