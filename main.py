'''
Crie um programa que leia a quantidade de combustível restante de um veículo em litros, o consumo médio de combustível do veículo em quilometros por litro e mostre o posto de gasolina mais distante dentro do limite de combustível do veículo. Considere que a distância dos quatro postos de gasolina mais próximos em quilometros é de 2, 15, 22 e 10,2.
'''

availableFuel = float(input('Digite a quantidade de combustível do veículo em litros: '))
km = float(input('Digite o consumo médio de combustível do veículo em quilômetros por litro: '))

distances = [2, 15, 22, 10.2]

result = -1

for distance in distances:
    requiredFuel = distance / km

    if requiredFuel <= availableFuel and distance > result:
        result = distance

if result > -1:
    print('O posto de gasolina mais distante dentro do limite atual de combustível está a {:.2f} Km de distância.'.format(n))
else:
    print('Não existe nenhum posto de gasolina dentro do limite atual de combustível.')
