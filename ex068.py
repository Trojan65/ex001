from random import randint
from time import sleep
cont = 0
print('-=-'*10)
print('VAMOS JOGAR PAR OU IMPAR')
while True:
    print('-=-'*10)
    n = int(input('Diga um valor: '))
    ip = ' '
    while ip not in 'PI':
        ip = str(input('Par ou Impar? [P/I] ')).upper().strip()
    sleep(0.5)
    if ip == 'I':
        ip = 'PAR'
    if ip == 'P':
        ip = 'IMPAR'
    n1 = randint(0, 10)
    soma = n1 + n
    if soma % 2 == 0:
        imparr = 'PAR'
    if soma % 2 == 1:
        imparr = 'IMPAR'
    print('-=-' * 10)
    print(f'Você jogou {n} e o computador {n1}. Total de {soma} DEU {imparr}')
    print('-=-' * 10)
    if ip == imparr:
        break
    cont += 1
    print('Você VENCEU!')
    print('Vamos jogar novamente...')
sleep(0.5)
print('Você PERDEU!')
print('-=-' * 10)
print(f'GAME OVER! Você venceu {cont} vezes.')
