from games import roleta
<<<<<<< Updated upstream
=======
from games import cacaNiqueis
>>>>>>> Stashed changes

UserId = input('Login: ')
input('Senha: ')

conta = 10

print('ROLETA ONLINE')
print('Conta: R$ :' + str(conta))
op = int(input('1. Jogar na Roleta\n2. Jogar no Caça níquel\n3. Adicionar fundos\n'))
if op==1:
    roleta.Game(conta)
<<<<<<< Updated upstream
if op==2:
=======
if op == 2:
    cacaNiqueis.Nique(conta)
if op==3:
>>>>>>> Stashed changes
    print('Adicionar fundos:\n')
    add = int(input('Valor: '))
    conta = conta + add
    print('\nBalanço total = ' + str(conta))
    input('Confirmar')



