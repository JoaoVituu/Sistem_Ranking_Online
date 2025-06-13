from games import roleta

UserId = input('Login: ')
input('Senha: ')

conta = 10

print('ROLETA ONLINE')
print('Conta: R$ :' + str(conta))
op = int(input('1. Jogar\n2. Adicionar fundos\n'))
if op==1:
    roleta.Game(conta)
if op==2:
    print('Adicionar fundos:\n')
    add = int(input('Valor: '))
    conta = conta + add
    print('\nBalanço total = ' + str(conta))
    input('Confirmar')



