valor_total = float(input("qual o valor da compra? R$ "))

print('''B - Boleto 
D - Débito 
C - Credito''')

formaPgto = input("Informe a forma de pagamento: ")

if formaPgto == "B":
    valor_total = valor_total * 0.9
    print(f"valor a pagar R$ {valor_total}")

elif formaPgto == "D":
    valor_total = valor_total * 0.95

    print(f"valor a pagar R$ {valor_total}")

else:
    print(f"valor a pagar R$ {valor_total}")