'''
Crie um programa que leia a quantidade de combustível restante de um veículo em litros, o consumo médio de combustível do veículo em quilometros por litro e mostre o posto de gasolina mais distante dentro do limite de combustível do veículo. Considere que a distância dos quatro postos de gasolina mais próximos em quilometros é de 2, 15, 22 e 10,2.
'''

fuel = float(input('Digite a quantidade de combustível do veículo em litros: '))
fuelConsumption = float(input('Digite o consumo médio de combustível do veículo em quilômetros por litro: '))

availableDistances = [2, 15, 22, 10.2]

availableDistances.sort()

distanceLimit = fuel * fuelConsumption

longestPossibleDistance = -1

for distance in availableDistances:
    if distance <= distanceLimit:
        longestPossibleDistance = distance

if longestPossibleDistance >= 0:
    print('O posto de gasolina mais distante dentro do limite atual de combustível está a {:.2f} Km de distância.'.format(longestPossibleDistance))
else:
    print('Não existe nenhum posto de gasolina dentro do limite atual de combustível.')
