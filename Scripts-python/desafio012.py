print('=== Desconto de 5%  ===')
print('-----------------------------------------------')
preco = float(input('Qual o preço do produto em R$? '))
novo = preco - (preco * 5 / 100)
print('------------------------------------------------------------------------------------------')
print('O produto custava R$ {} e agora passou à custar com o desconto R$ {}'.format(preco, novo))
print('------------------------------------------------------------------------------------------')
