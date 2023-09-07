# lógica para gravar o usuário
base_de_dados_do_usuario = {}
nome_do_usuario = input("Digite seu nome: ")
senha_do_usuario = input("Digite sua senha: ")
base_de_dados_do_usuario[nome_do_usuario] = senha_do_usuario

# lógica para autenticar o usuário
nome_do_usuario = input("Digite seu usuário: ")
senha_do_usuario = input("Digite asenha: ")

verificacao = False

if nome_do_usuario == base_de_dados_do_usuario.keys():
    verificacao = True
elif senha_do_usuario == base_de_dados_do_usuario[nome_do_usuario]:
    verificacao = True
else:
    verificacao = False

if verificacao:
    print("Login realizado com sucesso!")
else:
    print("Usuário ou senha incorreto! Tente novamente.")




