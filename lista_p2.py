minha_lista = ['Python', 'Java', 'C#', 'PHP', 'Java Script', 'Type Script']

pesquisa = "Java Script"

posicao = minha_lista.index(pesquisa)

print("A posição do item pesquisado é " + str(posicao))

nItens = len(minha_lista)

print(f"quantidade de itens {nItens}")

minha_lista.pop(3) # pop() exclui o ultimo item da lista
print(minha_lista)

print("---------------------------------")
minha_lista.clear()
print(minha_lista)