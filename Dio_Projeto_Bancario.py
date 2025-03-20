"""
    SAQUE EM CAIXA ELETRÔNICO

    ENTRADA
        Saldo fixo de R$ 1000
        Saque
    REQUISITO
        While True

    PROCESSAMENTO
        Solicitação de Saque:
            Opção para sacar, visualizar saldo e sair

        Valide se a operação pode ser realizada

    SAÍDA
        Estrado de retiradas
        Saldo atual
"""
lista_depositos = []
lista_saques = []
saldo_inicial = 500
limite_diario = 0

while True:
    menu = int(input('\n0. Deposito 1. Saque 2.Extrato 3.Sair | Opção: ' ))
    if limite_diario == 3:
        print("Voce excedeu o limite diário para saque, escolha outra opção!")
        break
    if menu == 0:
        deposito = float(input('Digite o valor acima de R$ 1 para depoosito: '))
            
        if deposito > 0:
            saldo_inicial+=(deposito)
            lista_depositos.append(deposito)
            print(f'\nDeposito Realizado! Valor disponível: R${saldo_inicial}')
        else:
            print(f'\nNão é possivel realizar o deposito, Valor abaixo do permitido!')
                
    elif menu == 1:
        saque = float(input('Valor do saque: '))

        if saque <= saldo_inicial:
            saldo_inicial  -= saque
            lista_saques.append(saque)
            limite_diario += 1
            print(f'Saque Realizado! Valor disponível: R${saldo_inicial}')
        else:
            print(f'\nNão é possível realizar o saque, Pois seu valor é de: R$ {saldo_inicial}')

    elif menu == 2:
        print(f'\nSaldo atual: R${saldo_inicial}')
        print('\nSaques realizados:')
        for saque in lista_saques:
            print(f'\n - R${saque}', end=' * ')
        for deposito in lista_depositos:
            print(f'\n + R${deposito}', end=' * ')
    else:
        menu == 3
        print('Finalizando Sistema!')
        break