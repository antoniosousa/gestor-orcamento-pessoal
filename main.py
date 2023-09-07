# aqui criamos nossa estrutura de dados chamada de dicionário
# funcionará como um banco de dados, mas ao pé da letra não é!
banco_usuario = {}

# aqui será o trecho de cadastro de usuarios de nosso sistema
# solicita o cadastro do nome
nome_do_usuario = input("Nome do usuário: ")
# salva o nome no dicionário
banco_usuario["nome"] = nome_do_usuario
# solicita o cadastro da senha
senha_do_usuario = input("Senha do usuário: ")
# salva a senha no dicionáro
banco_usuario["senha"] = senha_do_usuario

# aqui já é a parte do sistema que pergunta o usuário e a senha para depois verificarmos se estão corretos
nome_do_usuario_informado = input("Nome: ")
senha_do_usuario_informado = input("Senha: ")

# aqui é a verificação do que o usuário informou, nome e senha.
if banco_usuario["nome"] == nome_do_usuario_informado and banco_usuario["senha"] == senha_do_usuario_informado:
    print("Login realizado com sucesso!")
else:
    print("Usuário ou senha incorretos! Favor verificar e tentar novamente.")