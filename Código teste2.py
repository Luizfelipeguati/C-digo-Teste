print('Bem vindo(a) a loja de Luiz Felipe Catta Preta Guatimosim Ltda RU 4144632')

valorproduto = float(input('Entre com o valor do produto:'))
qtdproduto = int(input('Entre com o valor da quantidade:'))

valorfinal = valorproduto * qtdproduto
frete1 = 30.00
frete2 = 60.00
frete3 = 120.00
frete4 = 240.00

print('O Valor sem frete foi: R${:.2f}'.format(valorfinal))

if qtdproduto >=0 and qtdproduto <11:
    valorfinalcfrete1 = valorfinal + frete1
    print('O Valor com frete foi: R${:.2f}                 (frete de: R${:.2f})'.format(valorfinalcfrete1,frete1))
elif qtdproduto >=11 and qtdproduto <101:
    valorfinalcfrete2 = valorfinal + frete2
    print('O Valor com frete foi: R${:.2f}                 (frete de: R${:.2f})'.format(valorfinalcfrete2,frete2))
elif qtdproduto >=101 and qtdproduto <1001:
    valorfinalcfrete3 = valorfinal + frete3
    print('O Valor com frete foi: R${:.2f}                 (frete de: R${:.2f})'.format(valorfinalcfrete3,frete3))
else:
    valorfinalcfrete4 = valorfinal + frete4
    print('O Valor com frete foi: R${:.2f}                 (frete de: R${:.2f})'.format(valorfinalcfrete4,frete4))
