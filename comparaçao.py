###Criando uma lista
##Ivan,Gustavo, Tarso, Fabricio, Rafa, Gabriel, Victor

print("***Lista de nomes***\n")

nomes= input("Digite os nomes separados por virgulaa: ").split (",")

print("\nQuais operações você quer fazer;")
print("1 - Adicionar um nome")
print("2 - Remover um nome")
print("3 - Listar nome")
print("4 - Sair" )

while True:
    opcao =input("\nDigite a opção desejada (1-4):")

    if opcao == "1":
         print(f" foi adicionado á lista")

         
     elif opcao == "2":
        print(f"não está na lista")

    elif opcao =="3":
        print("\nlista de Nomes:")
