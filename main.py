'''
Crie um programa que leia a quantidade de combustível restante de um veículo em L, o consumo médio de combustível do veículo e a distância dos cinco postos de gasolina mais próximos em Km. Considere que a quantidade de combustível restante do veículo é de 2 L, cada litro de combustível permite que o veículo rode 8 Km e que as distâncias até os cinco postos de gasolina mais próximas são 2, 15, 22 e 10.2.
'''

c = float(input('Digite a quantidade de combustível do veículo: '))
d = [2, 15, 22, 10.2]
n = -1

d.sort(reverse=True)

for i in range(0, len(d)):
    g = d[i] / 8

    if g <= c and d[i] > n:
        n = d[i]

if n > -1:
    print('O posto de gasolina mais distante dentro do limite atual de combustível está a {} Km de distância.'.format(n))
else:
    print('Não existe nenhum posto de gasolina dentro do limite atual de combustível.')
    print(n)
