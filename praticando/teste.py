nome = 'Silvio'
print(f'{nome:#^50}')



extenso = 'Cento e cinquenta reais'

print(f'{extenso:*<50}')


numero = '10'

if numero.isnumeric():
    resultado = 10 + int(numero)
    print(resultado)
else:
    print('Não foi possível calcular não é número')