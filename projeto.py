class Livro:
    def __init__(self, titulo, escritor, ID, status):
        self.titulo = titulo
        self.escritor = escritor
        self.ID = ID
        self.status = status


class Usuario:
    def __init__(self, nome, ID):
        self.nome = nome
        self.ID = ID
        self.historico = []  # Lista para o histórico de livros emprestados pelo usuaario


class Biblioteca:
    def __init__(self):
        self.catalogo = []  # Lista de livros disponiveis
        self.usuarios = []  # Lista de usuários registrados

    #  Adicionar um livro ao catálogo da biblioteca
    def adicionar_livro(self, livro):
        self.catalogo.append(livro)

    # Adicionar um usuário à lista de usuários da biblioteca
    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f'O usuário {usuario.nome} foi registrado com sucesso.')

    # Emprestar um livro a um usuário
    def emprestar_livro(self, livro_id, usuario_id):
        livro = next((l for l in self.catalogo if l.ID == livro_id), None)
        usuario = next((u for u in self.usuarios if u.ID == usuario_id), None)

        if livro is None:
            print("Livro não encontrado.")
            return
        if usuario is None:
            print("Usuário não encontrado.")
            return

        if livro.status == 'disponivel':
            livro.status = 'emprestado'
            usuario.historico.append(livro)
            print(f'O livro "{livro.titulo}" foi emprestado para {usuario.nome}.')
        else:
            print('O livro não está disponível para empréstimo. Desculpe!')

    # Registrar a devolução de um livro
    def registrar_devolucao(self, livro, usuario):
        if livro in usuario.historico:
            livro.status = 'disponivel'
            usuario.historico.remove(livro)
            print(f'O livro "{livro.titulo}" foi devolvido por {usuario.nome}.')
        else:
            print('Opa, parece que este livro não está com este usuário.')

    # Permitir que um usuário devolva um livro
    def devolver_livro(self, livro_id, usuario_id):
        livro = next((l for l in self.catalogo if l.ID == livro_id), None)
        usuario = next((u for u in self.usuarios if u.ID == usuario_id), None)

        if livro is None:
            print("Livro não encontrado.")
            return
        if usuario is None:
            print("Usuário não encontrado.")
            return

        if livro.status == 'emprestado' and livro in usuario.historico:
            self.registrar_devolucao(livro, usuario)
        else:
            print("Este livro não está emprestado para este usuário.")

    # Remover um livro do catálogo da biblioteca
    def remover_livro(self, livro_id):
        livro = next((l for l in self.catalogo if l.ID == livro_id), None)
        if livro:
            self.catalogo.remove(livro)
            print(f'O livro "{livro.titulo}" foi removido do catálogo.')
        else:
            print("Livro não encontrado no catálogo.")

    # Procurar livros no catálogo da biblioteca
    def procurar_livro(self):
        print("\nProcurar Livro:")
        print("1. Por ID")
        print("2. Por Autor")
        print("3. Por Título")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            ID = int(input("Digite o ID do livro: "))
            livros_encontrados = [livro for livro in self.catalogo if livro.ID == ID]
        elif opcao == '2':
            autor = input("Digite o nome do autor: ")
            livros_encontrados = [livro for livro in self.catalogo if livro.escritor == autor]
        elif opcao == '3':
            titulo = input("Digite o título do livro: ")
            livros_encontrados = [livro for livro in self.catalogo if livro.titulo == titulo]
        else:
            print("Opção inválida.")
            return

        if livros_encontrados:
            print("\nLivros encontrados:")
            for livro in livros_encontrados:
                print(f"Título: {livro.titulo}, Autor: {livro.escritor}, ID: {livro.ID}, Status: {livro.status}")
        else:
            print("Nenhum livro encontrado.")

    # Verificar livros disponíveis para emprestimo
    def verificar_livros_disponiveis(self):
        livros_disponiveis = [livro for livro in self.catalogo if livro.status == 'disponivel']
        if livros_disponiveis:
            print("\nLivros disponíveis:")
            for livro in livros_disponiveis:
                print(f"Título: {livro.titulo}, Autor: {livro.escritor}, ID: {livro.ID}")
        else:
            print("Não há livros disponíveis no momento.")

    # Exibir os usuários registrados na biblioteca
    def ver_usuarios_registrados(self):
        if self.usuarios:
            print("\nUsuários Registrados:")
            for usuario in self.usuarios:
                print(f"Nome: {usuario.nome}, ID: {usuario.ID}")
        else:
            print("Não há usuários registrados no momento.")


# Biblioteca
biblioteca = Biblioteca()

# Menu
while True:
    print("\nBem-vindo à Biblioteca!")
    print("1. Adicionar Livro")
    print("2. Procurar Livro")
    print("3. Registrar Membro")
    print("4. Ver Usuários Registrados")
    print("5. Verificar Livros Disponíveis")
    print("6. Emprestar Livro")
    print("7. Devolver Livro")
    print("8. Remover Livro")
    print("9. Sair")

    escolha = input("Escolha uma opção: ")

    # Adicionar um novo livro
    if escolha == '1':
        titulo = input("Digite o título do livro: ")
        escritor = input("Digite o nome do escritor: ")
        ID = int(input("Digite o ID do livro: "))
        status = input("Digite o status do livro (disponivel ou emprestado): ")

        novo_livro = Livro(titulo, escritor, ID, status)
        biblioteca.adicionar_livro(novo_livro)

        print("\nInformações do novo livro:")
        print(f"Título do livro: {novo_livro.titulo}")
        print(f"Autor: {novo_livro.escritor}")
        print(f"ID: {novo_livro.ID}")
        print(f"Status: {novo_livro.status}")

    # Procurar por um livro 
    elif escolha == '2':
        biblioteca.procurar_livro()


    # Registrar um novo usuário 
    elif escolha == '3':
        nome = input("Digite o nome do usuário: ")
        ID = int(input("Digite o ID do usuário: "))
        novo_usuario = Usuario(nome, ID)
        biblioteca.adicionar_usuario(novo_usuario)


    # Exibir os usuários registrados
    elif escolha == '4':
        biblioteca.ver_usuarios_registrados()


    # Verificar livros para empréstimo
    elif escolha == '5':
        biblioteca.verificar_livros_disponiveis()


    # Emprestar um livro a um usuário
    elif escolha == '6':
        livro_id = int(input("Digite o ID do livro: "))
        usuario_id = int(input("Digite o ID do usuário: "))
        biblioteca.emprestar_livro(livro_id, usuario_id)
        

    # Devolver um livro
    elif escolha == '7':
        livro_id = int(input("Digite o ID do livro: "))
        usuario_id = int(input("Digite o ID do usuário: "))
        biblioteca.devolver_livro(livro_id, usuario_id)


    # Remover um livro do catálogo
    elif escolha == '8':
        livro_id = int(input("Digite o ID do livro que deseja remover: "))
        biblioteca.remover_livro(livro_id)


    # Sair do programa
    elif escolha == '9':
        print("Obrigado por usar a Biblioteca. Até mais!")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
