'''
Crie um programa que leia a quantidade de combustível restante de um veículo em litros, o consumo médio de combustível do veículo em quilometros por litro, a distância dos quatro postos de gasolina mais próximos em quilometros e mostre o posto de gasolina mais distante dentro do limite de combustível do veículo. Considere que a distância dos quatro postos de gasolina mais próximos é de 2, 15, 22 e 10,2 Km.
'''

c = float(input('Digite a quantidade atual de combustível do veículo: '))
km = float(input('Digite quantos quilometros o veículo é capaz de rodar a cada litro de combustível: '))

d = [2, 15, 22, 10.2]

n = -1

d.sort(reverse=True)

for i in d:
    g = i / km

    if g <= c and i > n:
        n = i

if n > -1:
    print('O posto de gasolina mais distante dentro do limite atual de combustível está a {:.2f} Km de distância.'.format(n))
else:
    print('Não existe nenhum posto de gasolina dentro do limite atual de combustível.')
