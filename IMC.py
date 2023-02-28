'''
Calculo de IMC - Índice de Massa Corporal

Qual é a sua altura em cm:
Qual é o seu peso em kg:


Menor que 18,5  -  Magreza
Entre 18,5 e 24,9  -  Normal
Entre 25,0 e 29,9  -  Sobrepeso
Entre 30,0 e 39,9  -  Obesidade
Maior que 40,0  -  Obesidade grave
'''

altura = float(input('Qual é a sua altura em cm? '))
peso = float(input('Qual é o seu peso em kg? '))
calculo = peso / (altura/100)**2
print(f"\nSeu IMC é: {calculo:.2f}")

if calculo < 18.5:
    print('Segundo a tabela IMC, foi constatado que o seu é: Magreza')
elif calculo >= 18.5 and calculo < 24.9:
    print('Segundo a tabela IMC, foi constatado que o seu é: Normal')
elif calculo >= 25.0 and calculo < 29.9:
    print('Segundo a tabela IMC, foi constatado que o seu é: Sobrepeso')
elif calculo >= 30.0 and calculo < 39.9:
    print('Segundo a tabela IMC, foi constatado que o seu é: Obesidade')
else:
    print('Segundo a tabela IMC, foi constatado que o seu é: Obesidade Grave')
