itens = {}

itens[1757] = {'nome': "Arroz", 'preco':18.50, 'quantidade':10}
itens[1789] = {'nome': "Feijão", 'preco':12.00, 'quantidade':20}


for i in itens:
    print(i)



for iten in itens.values():
    print(iten['nome'], iten['preco'], iten['quantidade'])


print('------------------------------------')
print(itens[1757]['nome'])    


print('\n', f'{"Verificando se a chave já existe no dicionário":*^100}')
novo_codigo = 1757
if novo_codigo in itens:
    print('Produto já está na lista')



print('Quantidade de itens: ', len(itens))


print('\n', f'{"venda":*^50}')
itens[1757]['quantidade'] = 5
itens[1789]['quantidade'] = 8

if itens.get(1730):
    itens.get(1730)['quantidade'] = 8
else:
    print('1730 não existe')    

print(itens)




print(f'{"":*^150}')
for chave in itens:
    print(chave)

for valores in itens.values():
    print(valores)    


for valores in itens.values():
    print(valores['nome'])


for osdois in itens.items():
    print(osdois)    

#a chave é a posição zero e o valor a posição um pois note que é gerado uma tupla
for osdois in itens.items():
    print(osdois[0], osdois[1])    



print('\n', f'{" Desempacotando ":#^100}')
for chave, valor in itens.items():
    print(chave, valor)    






print('\n', f'{" for com for ":=^100}')    
for chave, valor in itens.items():
    print('Produto', chave)
    for item_chave, item_valor in valor.items():
        print(f'\t{item_chave} - {item_valor}')