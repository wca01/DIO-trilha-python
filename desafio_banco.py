menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

'''

saldo = 0
limite = 500
extrato = ""
num_saques = 0
lim_saques = 3

while True:
    opcao = input(menu)

    if opcao  == 'd':
        vdeposito = float(input('Informe valor para depositar: '))

        if vdeposito > 0:
            saldo += vdeposito
            extrato += f'+ Depósito: R$ {vdeposito:.2f}\n'
        else:
            print("Valor inválido, Digite novamente.")
        
    elif opcao == 's':
        vsaque = float(input('Informe valor para sacar: '))
        excedeu_saldo =  vsaque > saldo
        excedeu_limite = vsaque > limite
        excedeu_saques = num_saques >= lim_saques

        
        if excedeu_saldo:
            print('Operação inválida. Saldo insulficiente.')

        elif excedeu_limite:
            print ('Operação inválida. Valor limite por saque excedido.')  

        elif excedeu_saques:
            print('Operação inválida. Limite de saques excedido.')

        elif vsaque > 0:
            saldo -= vsaque
            extrato += f'- Saque: R$ {vsaque:.2f}\n'
            num_saques += 1     # incrementa número de saques 
        
        else:
            print('Operação inválida. Digite valor de novo.')

    elif opcao == 'e':
        print('\n============EXTRATO============\n')
        print('\nNenhuma movimentação realizada.' if not extrato else extrato)
        print(f'\nLimite de saques: {num_saques} / {lim_saques}')
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('=================================')
    elif opcao == 'q':
        break
    else:
        print('Opção inválida. Por favor, selecione opção válida.')

