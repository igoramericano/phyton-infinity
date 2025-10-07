usuario_valido = True
senha_valida = True
conta_ativa = True

if usuario_valido:
    print('Usuário encontrado')
    if senha_valida:
        print('Senha correta')
        if conta_ativa:
            print('Login bem-sucedido.')
            print('Acesso liberado')
        else:
            print('Erro: a conta está inativa.')
    else:
        print('Erro: a senha está incorreta.')
else:
    print('Erro: o usuário não foi encontrado.')