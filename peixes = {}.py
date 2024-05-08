peixes = {}

while True:
    print("1. Adicionar informações sobre um peixe")
    print("2. Mostrar informações de um peixe")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome_peixe = input("Digite o nome do peixe: ")
        habitat = input("Digite o habitat do peixe: ")
        alimentacao = input("Digite a alimentação do peixe: ")
        peixes[nome_peixe] = {"habitat": habitat, "alimentacao": alimentacao}
        print("Informações do peixe adicionadas com sucesso!")
    elif opcao == '2':
        nome_peixe = input("Digite o nome do peixe para ver as informações: ")
        if nome_peixe in peixes:
            print("Habitat:", peixes[nome_peixe]["habitat"])
            print("Alimentação:", peixes[nome_peixe]["alimentacao"])
        else:
            print("Peixe não encontrado.")
    elif opcao == '3':
        break
    else:
        print("Opção inválida. Por favor, escolha novamente.")

# PEQUENO PROGRAMA DESENVOLVIDO COMO PROJETO PARA A EMPRESA DA FAMÍLIA, AQUI TENHO UMA BASE DE COMO FUNCIONARIA O PROGRAMA QUE PEDIRAM:
# - ADICIONAR INFORMAÇÕES DO PEIXE NO BANCO DE DADOS, - RETORNAR ESSAS INFORMAÇÕES CASO REQUISITADA PELO USUÁRIO DO PROGRAMA (APLICAÇÃO DA API)
# - FUTURAMENTE TENTAR APLICAR POR IA UMA PESQUISA AUTOMÁTICA QUE RETORNE OS MELHORES TRATAMENTOS PARA O PEIXE PESQUISADO
# - CRIAR EM JAVASCRIPT UMA INTERFACE PARA O PROGRAMA ATUALMENTE 

