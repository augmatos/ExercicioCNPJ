import cnpj



while True:
    while True:
        entrada = input('Digite o CNPJ para validação(xx.xxx.xxx/xxxx-xx): ')
        if len(entrada) != 18:
            print('Voce nao digitou o CNPJ corretamente.')
        else:
            break

    if cnpj.valida(entrada):
        print(f'{entrada} é válido')
    else:
        print(f'{entrada} é inválido')
