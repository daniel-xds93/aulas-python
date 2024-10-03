senha = input("Digite sua senha: ")

acesso = False

if senha == "admin":
    acesso = True


if acesso:
    print("Acesso autorizado!")
else:
    print("Acesso Negado!")