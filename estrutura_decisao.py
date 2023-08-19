valor_compra = float(input("Digite o valor da compra: R$ "))

parcelar = input("Vai parcelar (S) Sim | (N) Não: ")

if parcelar == 'N':
    valor_pagar = valor_compra * 0.9

    print(f"Valor a pagar R$ {valor_pagar}")

else:
    qtd_parcela = int(input("Digite a quantidade de parcelas: "))

    valor_parcela = valor_compra / qtd_parcela

    print(f"Valor total da compra: R$ {valor_compra}")
    print(f"Valor da parcela R$ {valor_parcela} quantidade de parcelas {qtd_parcela}")