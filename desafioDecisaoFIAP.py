funcao = input("digite sua função: adm, user, ou guest")
genero = input("qual seu genero: masc ou fem")

if funcao=="user":
    if genero=="masc":
        print("Olá usuário")
    elif genero == "fem":
        print("Olá usuária")
elif funcao=="adm":
    if genero=="masc":
        print("Olá admnistrador")
    elif genero == "fem":
        print("Olá admnistradora")
elif funcao=="guest":
        print("Olá visitante ")
else: print("Olá desconhecido")


