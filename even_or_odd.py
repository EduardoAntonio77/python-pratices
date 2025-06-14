while True:
    number = input('Digite um numero: ')
    try:
        number = int(number)
    except ValueError:
        print('Digite um valor valido.')
        continue

    if number % 2 == 0:
        print('Este valor é um numero par')
    else:
        print('Este valor é um numero impar')

    while True:
        question = input('Deseja rodar o programa mais uma vez (s/n)? ').lower().split()
        if question == 's':
            break
        else:
            print('Encerrando programa...')
            exit()
           