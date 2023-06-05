import random
print('Bem vindo ao Controle de Estoque da Bicicletaria do Rafael')
###################################################################
cadastro = []
while True:
    codigo = random.randint(0,1000)
    opcoes = int(input('Escolha a opção desejada:\n'
                   '1- Cadastrar peças\n'
                   '2- Consultar peças\n'
                   '3- Remover peças\n'
                   '4- Sair\n'
                   '>> '
                   ))
    
    def cadastrarPeca(codigo): 
        print('Você escolheu a opcão Cadastrar Peça')
        print(f'Código da peça - {codigo}')
        nome = input('Digite o nome da peça: ') 
        fabricante = input('Digite o fabricante: ') 
        valor = int(input('Digite o valor da peça: ')) 
        dicionario = {'Código'      : codigo, 
                        'Nome'    : nome, 
                        'Fabricante'   : fabricante, 
                        'Valor' : f'{valor}'}
        
        cadastro.append(dicionario.copy())

    def consultarPeca():
        while True:
            print('Você selecionou consultar peça')
            opcao = int(input('Escolha a opção desejada:\n'
                            '1- Consultar todas as peças\n'
                            '2- Consultar peças por código\n'
                            '3- Consultar peças por fabricante\n'
                            '4- Retornar\n'
                            '>> '
                            ))

            if opcao == 1:
                print('-------------------------------')
                print()
                for dicionario in cadastro:
                    for chave, valor in dicionario.items():
                        print(f'{chave} : {valor}')
                    print()
                print('-------------------------------')
            
            elif opcao == 2:
                codigo = int(input('Digite o código da peça: '))
                for dicionario in cadastro:
                    if codigo in dicionario.values():
                        print('-------------------------------')
                        for chave, valor in dicionario.items():
                            print(f'{chave} : {valor}')
                        print('-------------------------------')
            
            elif opcao == 3:
                fabricante = input('Digite o fabricante: ')
                for dicionario in cadastro:
                    if fabricante in dicionario.values():
                        print('-------------------------------')
                        for chave, valor in dicionario.items():
                            print(f'{chave} : {valor}')
                        print('-------------------------------')

            elif opcao == 4:
                break

            else:
                print('Você digitou uma opção inexistente\nTente novamente.')
                continue

    def removerPeca():
        remover = int(input('Digite o código da peça a ser removida: '))
        
        for dicionario in cadastro:
            if remover in dicionario.values():
                cadastro.remove(dicionario)

    if opcoes == 1:
        cadastrarPeca(codigo)
        continue
    elif opcoes == 2:
        consultarPeca()
    elif opcoes == 3:
        removerPeca()
    elif opcoes == 4:
        break
    else:
        print('Você não colocou a opcão correta\nTente novamente.')
        continue
