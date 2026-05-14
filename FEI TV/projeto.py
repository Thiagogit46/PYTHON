
import os

def menu_inicial():
    while True:
        print("="*50)
        print("BEM VINDO A MELHOR PLATAFORMA DE STREAMING DO MUNDO")
        print("="*50)
        print("1 - Criar conta")
        print("2 - Entrar na conta")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            criar()
            break
        elif opcao == "2":
            entrar()
            break
        elif opcao == "3":
            print("Obrigado por usar nossa plataforma. Até a próxima!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

def criar():
    print("Criar conta")
    usuario=input("Digite seu nome de usuário: ").strip()
    cpf=(input("Digite seu CPF: ")).strip()
    senha=input("Digite sua senha: ").strip()

    cpf_existente=False # variavel criada para restringir ciracao de mais de um cpf
    try:
        with open('cadastro.txt', 'r') as cadastro : 
            for linha_cadastro in cadastro:
                dados_cadastro=linha_cadastro.strip().split('|') #separa cpft e login por |
                if len(dados_cadastro)>=11 and cpf == dados_cadastro[1]: # len cadastros limita para que o cpf tenha 11 numeros
                    cpf_existente=True
                    break
    except FileNotFoundError:
        pass
    if cpf_existente:
        print("CPF, cadastrado a outro usuario.Tente novamente") #condicao caso cpf ja esteja criado 
    else:
        with open('cadastro.txt','a') as cadastro:
            cadastro.write(f'{usuario}|{cpf}|{senha}\n') #escreve o codigo no arquivo

        print("Usuario cadastrado com sucesso!!!")
        opcao=input("Deseja criar outra conta ? (s/n)").strip()
        
        while opcao !='n' :
            print("Criar conta")
            usuario=input("Digite seu nome de usuário: ").strip()
            cpf=(input("Digite seu CPF: ")).strip()
            senha=input("Digite sua senha: ").strip()

            cpf_existente=False
            try:
                with open('cadastro.txt', 'r') as cadastro :
                    for linha_cadastro in cadastro:
                        dados_cadastro=linha_cadastro.strip().split('|')
                        if len(dados_cadastro)>=2 and cpf == dados_cadastro[1]:
                            cpf_existente=True
                            break
            except FileNotFoundError:
                pass
            if cpf_existente:
                print("CPF, cadastrado a outro usuario.Tente novamente")
            else:
                with open('cadastro.txt','a') as cadastro:
                    cadastro.write(f'{usuario}|{cpf}|{senha}\n')

                print("Usuario cadastrado com sucesso!!!")
                opcao=input("Deseja criar outra conta ? ").strip()
                     
        else:
            while True:
                print("1- Entrar")
                print("2- Voltar ao Menu")
                opcao = input("Escolha uma opção: ")
                if opcao=="1":
                    entrar()
                    break
                elif opcao=="2":
                    menu_inicial()
                    break
                else:
                    print("Opcao Invalida. Tente Novamente")

def entrar():
    usuario=input("Digite seu usuario: ").strip()
    senha=input("Digite sua senha: ").strip()

    conta_encontrada= False #para definir se a conta esta ou nao no arquivo cadastro txt 
    try:
        with open('cadastro.txt','r') as arquivo:
            for linha in arquivo:
                linha=linha.strip()
                if not linha:
                    continue
                dados=linha.split("|")
                usuario_salvos=dados[0]
                senha_salvas=dados[2]
                if usuario_salvos ==usuario and senha_salvas==senha: # comando para ver se os dados escritos estao no carquivop txt 
                    conta_encontrada=True
                    break

    except FileNotFoundError:
        print("Nenhuma conta foi encontrada!")
        criar()
        return
    if conta_encontrada:
        menu_principal()
    else:
        print("Usuario ou senha incorreto. Tentar Novamente")
        return

def menu_principal():
    print("*"*50)
    print("Bem Vindo!!!!")
    print("1- Cadastrar Filme")
    print("2- Procurar Filme")
    print("3- Curtir e Discutir Filmes")
    print("4- Gerenciar Favoritos") 
    print("5- Sair")
    opcao=input("Escolha uma opcao: ").strip()
    if opcao =='1':
        cadastrar_filmes()
    elif opcao =='2':
        procurar()
    elif opcao=='3':
        curtir_descurtir()
    elif opcao=='4':
        gerenciar()
    elif opcao=='5':
        menu_inicial()

def cadastrar_filmes():
    nome = input("Nome do filme: ").strip()
    data = input("Data de lançamento: ").strip()
    diretor = input("Diretor: ").strip()
    faixa = input("Faixa etária: ").strip()

    filmes = carregar_filmes()               
    if buscar_filme(nome, filmes) != -1:  # le se os ddados do filme ja estao 
        print("Esse filme já está cadastrado!") 
        menu_principal()
#
    novo_filme = (nome, data, diretor, faixa, "0")   
    filmes.append(novo_filme)               
    salvar_filmes(filmes)
    print("Filme Cadastrado com sucesso")
    menu_principal()    

def buscar_filme(nome, filmes):
    for i in range(len(filmes)):             
        if filmes[i][0].lower() == nome.lower():
            return i 
    return -1              

def procurar():
    nome = input("Digite o nome do filme: ").strip()
    filmes = carregar_filmes()
    indice = buscar_filme(nome, filmes)

    if indice == -1:                         
        print("Filme não encontrado.")
    else:
        filme = filmes[indice]               
        print("Nome: " + filme[0])     
        print("Lançamento: " + filme[1])    
        print("Diretor: " + filme[2])      
        print("Faixa: " + filme[3])      
        print("Curtidas: " + filme[4])
        menu_principal()         


def curtir_descurtir():
    print("1- Curtir um filme")
    print("2- Descurtir um filme")
    print("3- Voltar ao Menu")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        nome   = input("Nome do filme que deseja curtir: ").strip()
        filmes = carregar_filmes()
        indice = buscar_filme(nome, filmes)

        if indice == -1:
            print("Filme não encontrado")
        else:
            filme        = filmes[indice]
            nova_curtida = str(int(filme[4]) + 1)
            filmes[indice] = (filme[0], filme[1], filme[2], filme[3], nova_curtida)
            salvar_filmes(filmes)
            print("Você curtiu '" + filme[0] + "'! Total: " + nova_curtida + " curtidas.")
        curtir_descurtir()

    elif opcao == "2":
        nome   = input("Nome do filme que deseja descurtir: ").strip()
        filmes = carregar_filmes()
        indice = buscar_filme(nome, filmes)
        if indice == -1:
            print("Filme não encontrado.")
        else:
            filme        = filmes[indice]
            curtidas_atual = int(filme[4])
            if curtidas_atual == 0:
                print("'" + filme[0] + "' já está com 0 curtidas.")
            else:
                nova_curtida = str(curtidas_atual - 1)
                filmes[indice] = (filme[0], filme[1], filme[2], filme[3], nova_curtida)
                salvar_filmes(filmes)
                print("Você descurtiu '" + filme[0] + "'! Total: " + nova_curtida + " curtidas.")
        curtir_descurtir()
    elif opcao == "3":
        menu_principal()
    else:
        print("Opção inválida.")
        curtir_descurtir()

def salvar_filmes(filmes):
    with open('filmes.txt','w') as salvar:
        for filme in filmes:
            linha=filme[0]+"|"+filme[1]+"|"+filme[2]+"|"+filme[3]+"|"+filme[4]
            salvar.write(linha + "\n")


def carregar_filmes():
    filmes = [] 
    try:
        with open('filmes.txt', 'r') as arquivo:
            for linha in arquivo:        
                linha = linha.strip()  
                if linha:               
                    dados = linha.split("|")  
                    
                    filme = (dados[0], dados[1], dados[2], dados[3], dados[4])
                    filmes.append(filme)
    except FileNotFoundError:
        pass                         
    return filmes




def gerenciar():
    print("1- Ver minhas listas")
    print("2- Criar nova lista")
    print("3- Renomear uma lista")
    print("4- Excluir uma lista")
    print("5- Adicionar filme a uma lista")
    print("6- Remover filme de uma lista")
    print("7- Voltar ao Menu")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        ver()
    elif opcao == "2":
        criar_lista()
    elif opcao == "3":
        renomear_lista()
    elif opcao == "4":
        excluir_lista()
    elif opcao == "5":
        adicionar_filme_lista()
    elif opcao == "6":
        remover()
    elif opcao == "7":
        menu_principal()
    else:
        print("Opção inválida.")
        gerenciar()

def carregar_favoritos():
    favoritos = []
    try:
        with open('favoritos.txt', 'r') as arquivo:
            for linha in arquivo:
                dados = linha.strip().split("|")
                nome_lista = dados[0]         
                if dados[1]:                  
                    filmes_lista = dados[1].split(",")  
                else:
                    filmes_lista = []        
                favoritos.append([nome_lista, filmes_lista])
    except FileNotFoundError:
        pass
    return favoritos


def salvar_favoritos(favoritos):
    with open('favoritos.txt', 'w') as arquivo:
        for lista in favoritos:
            filmes_str = ",".join(lista[1])   
            arquivo.write(lista[0] + "|" + filmes_str + "\n")

def ver():
    favoritos = carregar_favoritos()
    if not favoritos:
        print("\nVocê ainda não tem listas de favoritos.")
        gerenciar()
        return

    print("\n" + "="*50)
    print("        SUAS LISTAS DE FAVORITOS")
    print("="*50)

    filmes = carregar_filmes()
    for lista in favoritos:
        print("\n  Lista: " + lista[0])
        print("-"*40)
        if lista[1]:
            for nome_filme in lista[1]:
                indice = buscar_filme(nome_filme, filmes)
                if indice != -1:
                    f = filmes[indice]
                    print("  * " + f[0] + " (" + f[1] + ") | Dir: " + f[2] + " | Faixa: " + f[3] + " | Curtidas: " + f[4])
                else:
                    print("  * " + nome_filme)
        else:
            print("  (lista vazia)")
    print("="*50)
    input("\nPressione Enter para voltar...")
    gerenciar()


def criar_lista():
    nome_lista = input("Nome da nova lista: ").strip()
    if not nome_lista:
        print("O nome não pode ser vazio.")
        gerenciar()
        return

    favoritos = carregar_favoritos()
    for lista in favoritos:
        if lista[0].lower() == nome_lista.lower():
            print("Já existe uma lista com esse nome!")
            gerenciar()
            return

    favoritos.append([nome_lista, []])
    salvar_favoritos(favoritos)
    print("Lista '" + nome_lista + "' criada com sucesso!")
    gerenciar()


def renomear_lista():
    favoritos = carregar_favoritos()
    if not favoritos:
        print("Você não tem listas para renomear.")
        gerenciar()
        return

    print("\nSuas listas:")
    for i in range(len(favoritos)):
        print(str(i + 1) + "- " + favoritos[i][0])

    escolha = input("Número da lista para renomear: ").strip()
    if not escolha.isdigit() or int(escolha) < 1 or int(escolha) > len(favoritos):
        print("Opção inválida.")
        gerenciar()
        return

    indice     = int(escolha) - 1
    nome_atual = favoritos[indice][0]
    novo_nome  = input("Novo nome para '" + nome_atual + "': ").strip()

    if not novo_nome:
        print("O nome não pode ser vazio.")
        gerenciar()
        return

    for lista in favoritos:
        if lista[0].lower() == novo_nome.lower():
            print("Já existe uma lista com esse nome!")
            gerenciar()
            return

    favoritos[indice][0] = novo_nome
    salvar_favoritos(favoritos)
    print("Lista renomeada de '" + nome_atual + "' para '" + novo_nome + "'!")
    gerenciar()


def excluir_lista():
    favoritos = carregar_favoritos()
    if not favoritos:
        print("Você não tem listas para excluir.")
        gerenciar()
        return

    print("\nSuas listas:")
    for i in range(len(favoritos)):
        print(str(i + 1) + "- " + favoritos[i][0] + " (" + str(len(favoritos[i][1])) + " filmes)")

    escolha = input("Número da lista para excluir: ").strip()
    if not escolha.isdigit() or int(escolha) < 1 or int(escolha) > len(favoritos):
        print("Opção inválida.")
        gerenciar()
        return

    indice     = int(escolha) - 1
    nome_lista = favoritos[indice][0]
    confirmacao = input("Tem certeza que deseja excluir '" + nome_lista + "'? (s/n): ").strip().lower()

    if confirmacao != 's':
        print("Exclusão cancelada.")
        gerenciar()
        return

    favoritos.pop(indice)
    salvar_favoritos(favoritos)
    print("Lista '" + nome_lista + "' excluída com sucesso!")
    gerenciar()


def adicionar_filme_lista():
    favoritos = carregar_favoritos()
    if not favoritos:
        print("Você ainda não tem listas. Crie uma primeiro!")
        gerenciar()
        return

    print("\nSuas listas:")
    for i in range(len(favoritos)):
        print(str(i + 1) + "- " + favoritos[i][0])

    escolha = input("Número da lista: ").strip()
    if not escolha.isdigit() or int(escolha) < 1 or int(escolha) > len(favoritos):
        print("Opção inválida.")
        gerenciar()
        return

    indice_lista = int(escolha) - 1
    nome_filme   = input("Nome do filme para adicionar: ").strip()

    filmes = carregar_filmes()
    if buscar_filme(nome_filme, filmes) == -1:
        print("Filme não encontrado. Cadastre-o primeiro.")
        gerenciar()
        return

    if nome_filme in favoritos[indice_lista][1]:
        print("Esse filme já está na lista!")
    else:
        favoritos[indice_lista][1].append(nome_filme)
        salvar_favoritos(favoritos)
        print("'" + nome_filme + "' adicionado à lista '" + favoritos[indice_lista][0] + "'!")
    gerenciar()


def remover():
    favoritos = carregar_favoritos()
    if not favoritos:
        print("Você não tem listas.")
        gerenciar()
        return

    print("\nSuas listas:")
    for i in range(len(favoritos)):
        print(str(i + 1) + "- " + favoritos[i][0])

    escolha = input("Número da lista: ").strip()
    if not escolha.isdigit() or int(escolha) < 1 or int(escolha) > len(favoritos):
        print("Opção inválida.")
        gerenciar()
        return

    indice_lista = int(escolha) - 1
    lista_atual  = favoritos[indice_lista]

    if not lista_atual[1]:
        print("Essa lista está vazia!")
        gerenciar()
        return

    print("\nFilmes em '" + lista_atual[0] + "':")
    for i in range(len(lista_atual[1])):
        print(str(i + 1) + "- " + lista_atual[1][i])

    escolha_filme = input("Número do filme para remover: ").strip()
    if not escolha_filme.isdigit() or int(escolha_filme) < 1 or int(escolha_filme) > len(lista_atual[1]):
        print("Opção inválida.")
        gerenciar()
        return

    removido = lista_atual[1].pop(int(escolha_filme) - 1)
    salvar_favoritos(favoritos)
    print("'" + removido + "' removido da lista '" + lista_atual[0] + "'!")
    gerenciar()



print(menu_inicial())