produto = float(input('Valor do produto: R$'))
condicao = int(input('Condicao de pagamento:\n1 - a vista dinheiro/cheque\n2 - a vista no cartao\n3 - em 2x no cartao'
                     '\n4 - em 3 ou mais vezes no cartao\nDigite o numero da opcao"'))

print('Valor do produto R${}'.format(produto))
if condicao == 1:
    print('O valor do produto a vista com 10% de desconto, sera de R${:.2f}'.format(produto - (produto * 0.1)))
elif condicao == 2:
    print('O valor do produto a vista no cartao com 5% de desconto, sera de R${:.2f}'.format(produto - (produto * 5 / 100)))
elif condicao == 3:
    print('O valor do produto parcelado em 2x no cartao, sera de R${:.2f} por parcela'.format(produto / 2))
elif condicao == 4:
    vezes = int(input('Em quantas vezes voce gostaria de parcelar?'))
    parcela = ((produto * 20 / 100) + produto) / vezes
    print('O valor do produto parcelado em {}x no cartao com 20% de juros, sera de R${:.2f} por parcela'.format(vezes, parcela))
else:
    print('\033[31mOPCAO INVALIDA DE PAGAMENTO. TENTE NOVAMENTE')
