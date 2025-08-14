"""/*******************************************************************************
Autor: Enzo Cauã da Silva Barbosa
Componente Curricular: Algoritmos I
Concluido em: 21/04/2024
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
******************************************************************************************/"""

"""
> Este produto foi desenvolvido como avaliação do problema 1 da disciplina MI Algoritimos I - EXA854. 
> O produto solicitado foi um codigo para reaização da venda de ingressos para um show, que pudesse ser customizado e 
que ao fim das vendas, exibisse os resultados e quantidades de cada categoria.
> O codigo a seguir permite ao usuario configurar previamente o evento, podendo configurar a quantidade ingressos dispo-
niveis, o valor do ingresso inteiro, informar se havera um preço especial e tambem definir qual sera o preço especial.
> Durante o periodo de vendas, o usuario podera escolher o tipo de vendedor, o tipo de ingresso, o tipo de meia entrada
e no caso dos vendedores comissionado, exite a possibilidade de escolher a venda comissionada, que permite a venda de 10
ingressos de uma vez, garantindo assim uma cortesia para o vendedor, caso haja ingressos suficientes para isso, durante
a venda tambem é registrado a idade de todos os ingressos emitidos, exceto das cortesias dadas aos vendedores.
> Ao final das vendas sera exibido as quantidades de: ingressos emitidos e não emitidos, meias-entradas para estudante,
meias-entradas para outros criterios, inteiras, ingressos com preço especial (Equivalente na descrição do problema aos 
estudante de Engenharia da Computação), cortesias emitidas, cortesias emitidas para os vendedores comissionados, ingres-
sos vendidos pelos vendedores comissionados, total de dinheiro arrecadado, arrecadação por tipo de ingresso, tipo mais
vendido de ingresso e a media das idades dos compradores.
> Em todas as entradas existe a validação para que o so aceite entradas adequadas, impedindo que o codigo pare por erro
do usuario.
"""

# DECLARAÇÃO DE VARIAVEIS

soma_idade = 0
inteira = 0
meia = 0
meia_estudante = 0
meia_outros = 0
ing_preco_especial = 0
valor_especial = 0
cortesia = 0
vendedor_comum = 0
vendedor_comissionado = 0
contador = 1
cortesia_vendedor = 0


print(f'\033[36m{' SISTEMA DE VENDA DE INGRESSOS ':=^70}')

# CONFIGURAÇÕES DO EVENTO

print(f'\n{' CONFIGURAÇÕES DO EVENTO ':=^70}')
print(f'{'Informe os dados para o evento':^70}\033[m')

# Definição da quantidade de ingressos
ingressos_totais = str(input('Quantidade de Ingressos Disponíveis: '))

# Validação da entrada 'Ingressos Totais'
while not ingressos_totais.isdigit():
    if ingressos_totais == '':
        print('\033[31mERRO: Entrada Vazia! Digite um numero inteiro!\033[m\n')
        ingressos_totais = str(input('Quantidade de Ingressos Disponiveis: '))
    else:
        print('\033[31mERRO: Entrada Invalida! Digite um numero inteiro!\033[m\n')
        ingressos_totais = str(input('Quantidade de Ingressos Disponiveis: '))
ingressos_totais = int(ingressos_totais)  # Conversão de String para Inteiro
ingressos_restantes = ingressos_totais  # Valor inicial da variavel de controle

# Definição do valor do ingresso
valor_ingresso_input = str(input('Valor do Ingresso: R$').strip())

# Validação da entrada 'valor do ingresso'
while valor_ingresso_input == '':
    print('\033[31mERRO: Entrada vazia! Informe um valor!\033[m\n')
    valor_ingresso_input = str(input('Valor do Ingresso: R$').strip())
valor_ingresso_str = valor_ingresso_input.replace(',', '').replace('.', '')
while not valor_ingresso_str.isdigit():
    print('\033[31mERRO: Entrada Invalida! Informe um valor!\033[m\n')
    valor_ingresso_input = str(input('Valor do Ingresso: R$').strip())
    valor_ingresso_str = valor_ingresso_input.replace(',', '').replace('.', '')
valor_ingresso = float(valor_ingresso_input.replace(',', '.'))
# 'Valor_ingresso_input' refere-se ao valor que o usuario digitara.
# 'Valor_ingresso_str' refere-se ao valor digitado sem "," ou ".", ex:(Converte 2,2 para 22).
# 'Valor_ingresso' refere-se ao valor digitado convertido para float substituindo "," por ".".

# Definição se havera valor especial do ingressos
validar_ingresso_especial = str(input('\nHavera preço especial? [1] Sim | [2] Não: '))

# Validação da entrada de confimação do valor especial e preço do valor especial
while validar_ingresso_especial not in ['1', '2']:
    print('\033[31mERRO: Opção Invalida! Digite 1 ou 2!\033[m\n')
    validar_ingresso_especial = str(input('Havera preço especial? [1] Sim | [2] Não: '))


if not validar_ingresso_especial.isdigit():
    print('\033[31mERRO: Opção Invalida! Digite 1 ou 2!\033[m\n')
    validar_ingresso_especial = str(input('Havera preço especial? [1] Sim | [2] Não: '))

# Definição do valor especial do ingressos
elif validar_ingresso_especial == '1':
    valor_especial_input = str(input('Valor do Especial: R$').strip())

    # Validação da entrada 'valor especial'
    while valor_especial_input == '':
        print('\033[31mERRO: Entrada vazia! Informe um valor!\033[m\n')
        valor_especial_input = str(input('Valor do Especial: R$').strip())
    valor_especial_str = valor_especial_input.replace(',', '').replace('.', '')
    while not valor_especial_str.isdigit():
        print('\033[31mERRO: Entrada Invalida! Informe um valor!\033[m\n')
        valor_especial_input = str(input('Valor do Especial: R$').strip())
        valor_especial_str = valor_especial_input.replace(',', '').replace('.', '')
    valor_especial = float(valor_especial_input.replace(',', '.'))

elif validar_ingresso_especial == '2':
    print('Não havera preço especial!')

# SISTEMA DE VENDAS

# Enquanto houver ingressos disponiveis o programa sera executado, a menos que seja selecionado a opção para encerrar.
while ingressos_restantes > 0:
    print(f'\n\033[36m{' VENDA DE INGRESSO ':=^70}')
    print(f'\033[35m{'Ingressos Restantes: {}'.format(ingressos_restantes):^70}')

    # Escolha do Vendedor
    print(f'\033[36m{' Vendedores ':-^70}')
    print('[ 1 ] Cortesia \n[ 2 ] Vendedor Comum \n[ 3 ] Vendedor Comissionado \n[ 4 ] Encerrar Vendas')
    vendedor = str(input('\033[36mEscolha o vendedor: '))

    # Validação da entrada 'Vendedor'.
    while not vendedor.isdigit():
        if vendedor == '':
            print('\033[31mERRO: Entrada vazia! Informe um numero!\033[m\n')
            vendedor = str(input('\033[36mEscolha o vendedor: '))
        else:
            print('\033[31mERRO: Entrada Invalida! Informe um numero!\033[m\n')
            vendedor = str(input('\033[36mEscolha o vendedor: '))
    while vendedor not in ['1', '2', '3', '4']:
        print('\033[31mERRO: Entrada Invalida! Informe um numero valido!\033[m\n')
        vendedor = str(input('\033[36mEscolha o vendedor: '))
    print('-' * 70)

    # VENDAS POR TIPO DE VENDEDOR

    # Emissão de Cortesia
    if vendedor == '1':
        print(f'\033[35m{'Tipo de Vendedor: [CORTESIA]':^70}\033[36m')
        print('-' * 70)

        # Registro de Idade
        idade = str(input('\033[36mInforme a idade do comprador: '))

        # Validação da Idade
        while not idade.isdigit():
            if idade == '':
                print('\033[31mERRO: Entrada vazia! Informe um numero!\033[m\n')
                idade = str(input('\033[36mInforme a idade do comprador: '))
            else:
                print('\033[31mERRO: Entrada Invalida! Informe um numero!\033[m\n')
                idade = str(input('\033[36mInforme a idade do comprador: '))
        idade = int(idade)

        # Variaveis Acumuladoras
        soma_idade += idade  # Soma das idades
        cortesia += 1  # Quantidade de Cortesias emitidas
        ingressos_restantes -= 1  # Ingresso vendido

    # Venda por Vendedor Comum
    if vendedor == '2':
        print(f'\033[35m{'Tipo de Vendedor: [VENDEDOR COMUM]':^70}')

        # Escolha do Tipo de Ingresso
        print(f'\033[36m{' Tipos de Ingresso ':-^70}')
        print('[ 1 ] Inteira \n[ 2 ] Meia \n[ 3 ] Preço Especial \n[ 4 ] Cancelar Venda')

        # Alerta caso não haja valor especial para o evento.
        if validar_ingresso_especial == '2':
            print('\033[33mATENÇÃO: Preço Especial Indisponivel para este evento\033[36m')

        # Escolha do Tipo de Ingresso
        tipo_ingresso = str(input('Escolha o Tipo de Ingresso: '))

        # Validação da entrada 'Tipo de Ingresso'.
        while not tipo_ingresso.isdigit():
            if tipo_ingresso == '':
                print('\033[31mERRO: Entrada vazia! Informe um numero!\033[m\n')
                tipo_ingresso = str(input('\033[36mEscolha o Tipo de Ingresso: '))
            else:
                print('\033[31mERRO: Entrada Invalida! Informe um numero!\033[m\n')
                tipo_ingresso = str(input('\033[36mEscolha o Tipo de Ingresso: '))
        while tipo_ingresso not in ['1', '2', '3', '4']:
            print('\033[31mERRO: Entrada Invalida! Informe um numero valido!\033[m\n')
            tipo_ingresso = str(input('\033[36mEscolha o tipo de ingresso: '))
        print('-' * 70)

        # VENDA POR TIPO DE INGRESSO - Vendedor Comum

        # Venda de inteira - Vendedor Comum
        if tipo_ingresso == '1':
            print(f'\033[35m{'Tipo de Ingresso: [INTEIRA]':^70}\033[36m')
            print('-' * 70)

            # Registro de Idade
            idade = str(input('\033[36mInforme a idade do comprador: '))

            # Validação da Idade
            while not idade.isdigit():
                if idade == '':
                    print('\033[31mERRO: Entrada vazia! Informe um numero!\033[m\n')
                    idade = str(input('\033[36mInforme a idade do comprador: '))
                else:
                    print('\033[31mERRO: Entrada Invalida! Informe um numero!\033[m\n')
                    idade = str(input('\033[36mInforme a idade do comprador: '))
            idade = int(idade)

            # Variaveis Acumuladoras
            soma_idade += idade  # Soma das idades
            inteira += 1  # Quantidade de Inteiras vendidas
            vendedor_comum += 1  # Quantidade de Vendas de Vendedores Comuns
            ingressos_restantes -= 1  # Ingresso vendido

        # Venda de Meia - Vendedor Comum
        if tipo_ingresso == '2':
            print(f'\033[35m{'Tipo de Ingresso: [MEIA]':^70}\033[36m')
            print('-' * 70)

            # Compravação de Meia
            comprovante = str(input('Possui Comprovação de Meia Entrada? [S / N]'))

            # Validação da Entrada 'Comprovante'
            while comprovante not in 'SsNn':
                print('\033[31mERRO: Entrada Invalida! Informe um S ou N!\033[m\n')
                comprovante = str(input('\033[36mPossui Comprovação de Meia Entrada? [S / N]'))

            # Venda somente com comprovação de meia
            if comprovante in 'Ss':

                # Escolha do Tipo de Meia
                print(f'\033[36m{' Tipos de Meia ':-^70}')
                print('[ 1 ] Estudante \n[ 2 ] Outros Criterios \n[ 3 ] Cancelar Venda')
                tipo_meia = str(input('Escolha o Tipo de Meia:'))

                # Validação da entrada 'Tipo de Meia'.
                while not tipo_meia.isdigit():
                    if tipo_meia == '':
                        print('\033[31mERRO: Entrada vazia! Informe um numero!\033[m\n')
                        tipo_meia = str(input('\033[36mEscolha o Tipo de Meia: '))
                    else:
                        print('\033[31mERRO: Entrada Invalida! Informe um numero!\033[m\n')
                        tipo_meia = str(input('\033[36mEscolha o Tipo de Meia: '))
                while tipo_meia not in ['1', '2', '3']:
                    print('\033[31mERRO: Entrada Invalida! Informe 1 ou 2!\033[m\n')
                    tipo_meia = str(input('\033[36mEscolha o Tipo de Meia: '))

                # Venda de Meia por Tipo - Vendedor Comum
                if tipo_meia == '1':
                    meia_estudante += 1
                elif tipo_meia == '2':
                    meia_outros += 1

                # Cancela a venda
                elif tipo_meia == '3':
                    print(f'\n\033[31m{'Venda Não Relizada'}')
                    continue

                # Registro de Idade
                idade = str(input('\033[36mInforme a idade do comprador: '))

                # Validação da Idade
                while not idade.isdigit():
                    if idade == '':
                        print('\033[31mERRO: Entrada vazia! Informe um numero!\033[m\n')
                        idade = str(input('\033[36mInforme a idade do comprador: '))
                    else:
                        print('\033[31mERRO: Entrada Invalida! Informe um numero!\033[m\n')
                        idade = str(input('\033[36mInforme a idade do comprador: '))
                idade = int(idade)

                # Variaveis Acumuladoras
                soma_idade += idade  # Soma das idades
                meia += 1  # Quantidade de Meias vendidas
                vendedor_comum += 1  # Quantidade de Vendas de Vendedores Comuns
                ingressos_restantes -= 1  # Ingresso vendido

            # Não realiza a venda caso não haja comprovante
            elif comprovante in 'Nn':
                print(f'\033[31m{'Venda Não Relizada'}')

        # Venda de Preço Especial - Vendedor Comum
        if tipo_ingresso == '3':

            # So realiza a venda do ingresso especial, caso o usuario tenha escolhido ter um preço especial
            if validar_ingresso_especial == '1':
                print(f'\033[35m{'Tipo de Ingresso: [PREÇO ESPECIAL]':^70}\033[36m')
                print('-' * 70)

                # Compravação de Preço Especial
                comprovante = str(input('Possui Comprovação de Preço Especial? [S / N]'))

                # Validação da Entrada 'Comprovante'
                while comprovante not in 'SsNn':
                    print('\033[31mERRO: Entrada Invalida! Informe um S ou N!\033[m\n')
                    comprovante = str(input('\033[36mPossui Comprovação de Preço Especial? [S / N]'))

                # Venda somente com comprovação de preço especial
                if comprovante in 'Ss':

                    # Registro de Idade
                    idade = str(input('\033[36mInforme a idade do comprador: '))

                    # Validação da Idade
                    while not idade.isdigit():
                        if idade == '':
                            print('\033[31mERRO: Entrada vazia! Informe um numero!\033[m\n')
                            idade = str(input('\033[36mInforme a idade do comprador: '))
                        else:
                            print('\033[31mERRO: Entrada Invalida! Informe um numero!\033[m\n')
                            idade = str(input('\033[36mInforme a idade do comprador: '))
                    idade = int(idade)

                    # Variaveis Acumuladoras
                    soma_idade += idade  # Soma das idades
                    ing_preco_especial += 1  # Quantidade de preço especial vendidos
                    vendedor_comum += 1  # Quantidade de Vendas de Vendedores Comuns
                    ingressos_restantes -= 1  # Ingresso vendido

                # Não realiza a venda caso não haja comprovante
                elif comprovante in 'Nn':
                    print(f'\033[31m{'Venda Não Relizada'}')

            # Não realiza a venda, caso o usuario tenha escolhido não ter preço especial
            elif validar_ingresso_especial == '2':
                print(f'\033[33m{'Preço Especial Indisponivel!'}')

        # Cancela a venda
        if tipo_ingresso == '4':
            print(f'\n\033[31m{'Venda Não Relizada'}')
            continue

    # Venda por Vendedor Comissionado
    if vendedor == '3':
        print(f'\033[35m{'Tipo de Vendedor: [VENDEDOR COMISSIONADO]':^70}')

        # Escolha do tipo de venda comissionada.
        print(f'\033[36m{' Tipos de Venda Comissionada ':-^70}')
        print('[ 1 ] Individual \n[ 2 ] Comissionada (10x Ingresso) \n[ 3 ] Cancelar Venda')
        print(f'''\033[33m{'''Atenção: A venda comissionada emite 10 ingresso por vez, sera 
necessario informar os dados de todos os compradores de uma unica vez!'''}\033[36m''')

        # Escolha do Tipo de Venda Comissionada
        tipo_venda = str(input('Escolha o Tipo de Venda: '))

        # Validação da entrada 'Tipo de Venda'.
        while not tipo_venda.isdigit():
            if tipo_venda == '':
                print('\033[31mERRO: Entrada vazia! Informe um numero!\033[m\n')
                tipo_venda = str(input('\033[36mEscolha o Tipo de Venda: '))
            else:
                print('\033[31mERRO: Entrada Invalida! Informe um numero!\033[m\n')
                tipo_venda = str(input('\033[36mEscolha o Tipo de Venda: '))
        while vendedor not in ['1', '2', '3']:
            print('\033[31mERRO: Entrada Invalida! Informe um numero valido!\033[m\n')
            vendedor = str(input('\033[36mEscolha o tipo de venda: '))
        print('-' * 70)

        # VENDA POR TIPO DE VENDA COMISSIONADA

        # Venda Individual
        if tipo_venda == '1':
            print(f'\033[35m{'Tipo de Venda: [Individual]':^70}\033[36m')
            print('-' * 70)

            # Escolha do Tipo de Ingresso
            print(f'\033[36m{' Tipos de Ingresso ':-^70}')
            print('[ 1 ] Inteira \n[ 2 ] Meia \n[ 3 ] Preço Especial \n [ 4 ] Cancelar Venda')

            # Alerta caso não haja valor especial para o evento.
            if validar_ingresso_especial == '2':
                print('\033[33mATENÇÃO: Preço Especial Indisponivel para este evento\033[36m')

            # Escolha do Tipo de Ingresso
            tipo_ingresso = str(input('Escolha o Tipo de Ingresso: '))

            # Validação da entrada 'Tipo de Ingresso'.
            while not tipo_ingresso.isdigit():
                if tipo_ingresso == '':
                    print('\033[31mERRO: Entrada vazia! Informe um numero!\033[m\n')
                    tipo_ingresso = str(input('\033[36mEscolha o Tipo de Ingresso: '))
                else:
                    print('\033[31mERRO: Entrada Invalida! Informe um numero!\033[m\n')
                    tipo_ingresso = str(input('\033[36mEscolha o Tipo de Ingresso: '))
            while tipo_ingresso not in ['1', '2', '3', '4']:
                print('\033[31mERRO: Entrada Invalida! Informe um numero valido!\033[m\n')
                tipo_ingresso = str(input('\033[36mEscolha o tipo de ingresso: '))
            print('-' * 70)

            # VENDA POR TIPO DE INGRESSO - Vendedor Comissionado

            # Venda de inteira - Vendedor Comissionado
            if tipo_ingresso == '1':
                print(f'\033[35m{'Tipo de Ingresso: [INTEIRA]':^70}\033[36m')
                print('-' * 70)

                # Registro de Idade
                idade = str(input('\033[36mInforme a idade do comprador: '))

                # Validação da Idade
                while not idade.isdigit():
                    if idade == '':
                        print('\033[31mERRO: Entrada vazia! Informe um numero!\033[m\n')
                        idade = str(input('\033[36mInforme a idade do comprador: '))
                    else:
                        print('\033[31mERRO: Entrada Invalida! Informe um numero!\033[m\n')
                        idade = str(input('\033[36mInforme a idade do comprador: '))
                idade = int(idade)

                # Variaveis Acumuladoras# Variaveis Acumuladoras
                soma_idade += idade  # Soma das idades
                inteira += 1  # Quantidade de Inteiras vendidas
                vendedor_comissionado += 1  # Quantidade de Vendas de Vendedores Comissionado
                ingressos_restantes -= 1  # Ingresso vendido

            # Venda de Meia - Vendedor Comissionado
            if tipo_ingresso == '2':
                print(f'\033[35m{'Tipo de Ingresso: [MEIA]':^70}\033[36m')
                print('-' * 70)

                # Compravação de Meia
                comprovante = str(input('Possui Comprovação de Meia Entrada? [S / N]'))

                # Validação da Entrada 'Comprovante'
                while comprovante not in 'SsNn':
                    print('\033[31mERRO: Entrada Invalida! Informe um S ou N!\033[m\n')
                    comprovante = str(input('\033[36mPossui Comprovação de Meia Entrada? [S / N]'))

                # Venda somente com comprovação de meia
                if comprovante in 'Ss':

                    # Escolha do Tipo de Meia
                    print(f'\033[36m{' Tipos de Meia ':-^70}')
                    print('[ 1 ] Estudante \n[ 2 ] Outros Criterios \n[ 3 ] Cancelar Venda')
                    tipo_meia = str(input('Escolha o Tipo de Meia:'))

                    # Validação da entrada 'Tipo de Meia'.
                    while not tipo_meia.isdigit():
                        if tipo_meia == '':
                            print('\033[31mERRO: Entrada vazia! Informe um numero!\033[m\n')
                            tipo_meia = str(input('\033[36mEscolha o Tipo de Meia: '))
                        else:
                            print('\033[31mERRO: Entrada Invalida! Informe um numero!\033[m\n')
                            tipo_meia = str(input('\033[36mEscolha o Tipo de Meia: '))
                    while tipo_meia not in ['1', '2']:
                        print('\033[31mERRO: Entrada Invalida! Informe 1 ou 2!\033[m\n')
                        tipo_meia = str(input('\033[36mEscolha o Tipo de Meia: '))

                    # Venda de Meia por Tipo - Vendedor Comissionado
                    if tipo_meia == '1':
                        meia_estudante += 1
                    elif tipo_meia == '2':
                        meia_outros += 1

                    # Cancela a venda
                    elif tipo_meia == '3':
                        print(f'\n\033[31m{'Venda Não Relizada'}')
                        continue

                    # Registro de Idade
                    idade = str(input('\033[36mInforme a idade do comprador: '))

                    # Validação da Idade
                    while not idade.isdigit():
                        if idade == '':
                            print('\033[31mERRO: Entrada vazia! Informe um numero!\033[m\n')
                            idade = str(input('\033[36mInforme a idade do comprador: '))
                        else:
                            print('\033[31mERRO: Entrada Invalida! Informe um numero!\033[m\n')
                            idade = str(input('\033[36mInforme a idade do comprador: '))
                    idade = int(idade)

                    # Variaveis Acumuladoras
                    soma_idade += idade  # Soma das idades
                    meia += 1  # Quantidade de Meias vendidas
                    vendedor_comissionado += 1  # Quantidade de Vendas de Vendedores Comissionados
                    ingressos_restantes -= 1  # Ingresso vendido

                # Não realiza a venda caso não haja comprovante
                elif comprovante in 'Nn':
                    print(f'\033[31m{'Venda Não Relizada'}')

            # Venda de Preço Especial - Vendedor Comissionado
            if tipo_ingresso == '3':

                # So realiza a venda do ingresso especial, caso o usuario tenha escolhido ter um preço especial
                if validar_ingresso_especial == '1':
                    print(f'\033[35m{'Tipo de Ingresso: [PREÇO ESPECIAL]':^70}\033[36m')
                    print('-' * 70)

                    # Compravação de Preço Especial
                    comprovante = str(input('Possui Comprovação de Preço Especial? [S / N]'))

                    # Validação da Entrada 'Comprovante'
                    while comprovante not in 'SsNn':
                        print('\033[31mERRO: Entrada Invalida! Informe um S ou N!\033[m\n')
                        comprovante = str(input('\033[36mPossui Comprovação de Preço Especial? [S / N]'))

                    # Venda somente com comprovação de preço especial
                    if comprovante in 'Ss':

                        # Registro de Idade
                        idade = str(input('\033[36mInforme a idade do comprador: '))

                        # Validação da Idade
                        while not idade.isdigit():
                            if idade == '':
                                print('\033[31mERRO: Entrada vazia! Informe um numero!\033[m\n')
                                idade = str(input('\033[36mInforme a idade do comprador: '))
                            else:
                                print('\033[31mERRO: Entrada Invalida! Informe um numero!\033[m\n')
                                idade = str(input('\033[36mInforme a idade do comprador: '))
                        idade = int(idade)

                        # Variaveis Acumuladoras
                        soma_idade += idade  # Soma das idades
                        ing_preco_especial += 1  # Quantidade de Meias vendidas
                        vendedor_comissionado += 1  # Quantidade de Vendas de Vendedores Comissionados
                        ingressos_restantes -= 1  # Ingresso vendido

                    # Não realiza a venda caso não haja comprovante
                    elif comprovante in 'Nn':
                        print(f'\033[31m{'Venda Não Relizada'}')

                # Não realiza a venda, caso o usuario tenha escolhido não ter preço especial
                elif validar_ingresso_especial == '2':
                    print(f'\033[33m{'Preço Especial Indisponivel!'}')

            # Cancela a Venda
            if tipo_ingresso == '4':
                print(f'\n\033[31m{'Venda Não Relizada'}')
                continue

        # Venda Comissionada: Vende 10 ingresso de uma so vez e emite uma cortesia para o vendedor.
        elif tipo_venda == '2':

            # Condição para so permite a venda comissionada caso haja no minimo 11 ingressos restantes
            if ingressos_restantes >= 11:
                print(f'\033[35m{'Tipo de Venda: [COMISSIONADA]':^70}\033[36m')
                print('-' * 70)
                print(f'\033[33m{'Atenção: Sera necessario informar os dados dos ingressos em sequencia!':^70}\033[36m')

                # Verficação se ha comprovanção para todos os ingressos
                comprovante = str(input('Todos os ingressos possuem comprovante (S/N)? '))
                while comprovante not in 'SsNn':
                    print('\033[31mERRO: Entrada Invalida! Informe um S ou N!\033[m\n')
                    comprovante = str(input('\033[36mPossui Comprovação de Meia Entrada? [S / N]'))

                # Venda somente se todos os ingressos tiverem comprovação
                if comprovante in 'Ss':

                    # Enquanto a quantidade de ingressos for < 10 pergunta a idade e o tipo de ingresso
                    while contador <= 10:

                        # Escolha do Tipo de Ingresso
                        print(f'\033[36m{' Tipos de Ingresso ':-^70}')
                        print('[ 1 ] Inteira \n[ 2 ] Meia \n[ 3 ] Preço Especial')

                        # Alerta caso não haja valor especial para o evento.
                        if validar_ingresso_especial == '2':
                            print('\033[33mATENÇÃO: Preço Especial Indisponivel para este evento\033[36m')

                        # Escolha do Tipo de Ingresso
                        tipo_ingresso = str(input('Escolha o Tipo de Ingresso: '))

                        # Validação da entrada 'Tipo de Ingresso'.
                        while not tipo_ingresso.isdigit():
                            if tipo_ingresso == '':
                                print('\033[31mERRO: Entrada vazia! Informe um numero!\033[m\n')
                                tipo_ingresso = str(input('\033[36mEscolha o Tipo de Ingresso: '))
                            else:
                                print('\033[31mERRO: Entrada Invalida! Informe um numero!\033[m\n')
                                tipo_ingresso = str(input('\033[36mEscolha o Tipo de Ingresso: '))
                        while tipo_ingresso not in ['1', '2', '3']:
                            print('\033[31mERRO: Entrada Invalida! Informe um numero valido!\033[m\n')
                            tipo_ingresso = str(input('\033[36mEscolha o tipo de ingreso: '))
                        print('-' * 70)

                        # Venda de inteira - Vendedor Comissionado
                        if tipo_ingresso == '1':
                            print(f'\033[35m{'Tipo de Ingresso: [INTEIRA]':^70}\033[36m')
                            print('-' * 70)
                            # Registro de Idade
                            idade = str(input('\033[36mInforme a idade do {}º comprador: '.format(contador)))

                            # Validação da Idade
                            while not idade.isdigit():
                                if idade == '':
                                    print('\033[31mERRO: Entrada vazia! Informe um numero!\033[m\n')
                                    idade = str(input('\033[36mInforme a idade do {}º comprador: '.format(contador)))
                                else:
                                    print('\033[31mERRO: Entrada Invalida! Informe um numero!\033[m\n')
                                    idade = str(input('\033[36mInforme a idade do {}º comprador: '.format(contador)))
                            idade = int(idade)

                            # Variaveis Acumuladoras
                            soma_idade += idade  # Soma das idades
                            inteira += 1  # Quantidade de Inteiras vendidas
                            vendedor_comissionado += 1  # Quantidade de Vendas de Vendedores Comissionado
                            ingressos_restantes -= 1  # Ingresso vendido
                            contador += 1  # Contador dos ingressos comissionados

                        # Venda de Meia - Vendedor Comissionado
                        if tipo_ingresso == '2':
                            print(f'\033[35m{'Tipo de Ingresso: [MEIA]':^70}\033[36m')
                            print('-' * 70)

                            # Escolha do Tipo de Meia
                            print(f'\033[36m{' Tipos de Meia ':-^70}')
                            print('[ 1 ] Estudante \n[ 2 ] Outros Criterios')
                            tipo_meia = str(input('Escolha o Tipo de Meia:'))

                            # Validação da entrada 'Tipo de Meia'.
                            while not tipo_meia.isdigit():
                                if tipo_meia == '':
                                    print('\033[31mERRO: Entrada vazia! Informe um numero!\033[m\n')
                                    tipo_meia = str(input('\033[36mEscolha o Tipo de Meia: '))
                                else:
                                    print('\033[31mERRO: Entrada Invalida! Informe um numero!\033[m\n')
                                    tipo_meia = str(input('\033[36mEscolha o Tipo de Meia: '))
                            while tipo_meia not in ['1', '2']:
                                print('\033[31mERRO: Entrada Invalida! Informe 1 ou 2!\033[m\n')
                                tipo_meia = str(input('\033[36mEscolha o Tipo de Meia: '))

                            # Venda de Meia por Tipo - Vendedor Comissionado
                            if tipo_meia == '1':
                                meia_estudante += 1
                            elif tipo_meia == '2':
                                meia_outros += 1

                            # Registro de Idade
                            idade = str(input('\033[36mInforme a idade do {}º comprador: '.format(contador)))

                            # Validação da Idade
                            while not idade.isdigit():
                                if idade == '':
                                    print('\033[31mERRO: Entrada vazia! Informe um numero!\033[m\n')
                                    idade = str(
                                        input('\033[36mInforme a idade do {}º comprador: '.format(contador)))
                                else:
                                    print('\033[31mERRO: Entrada Invalida! Informe um numero!\033[m\n')
                                    idade = str(
                                        input('\033[36mInforme a idade do {}º comprador: '.format(contador)))
                            idade = int(idade)

                            # Variaveis Acumuladoras
                            soma_idade += idade  # Soma das idades
                            meia += 1  # Quantidade de Meias vendidas
                            vendedor_comissionado += 1  # Quantidade de Vendas de Vendedores Comissionados
                            ingressos_restantes -= 1  # Ingresso vendido
                            contador += 1  # Contador dos ingressos comissionados

                        # Venda de Preço Especial - Vendedor Comissionado
                        if tipo_ingresso == '3':

                            # So realiza a venda do ingresso especial, caso o usuario tenha escolhido ter preço especial
                            if validar_ingresso_especial == '1':
                                print(f'\033[35m{'Tipo de Ingresso: [PREÇO ESPECIAL]':^70}\033[36m')
                                print('-' * 70)

                                # Registro de Idade
                                idade = str(input('\033[36mInforme a idade do {}º comprador: '.format(contador)))

                                # Validação da Idade
                                while not idade.isdigit():
                                    if idade == '':
                                        print('\033[31mERRO: Entrada vazia! Informe um numero!\033[m\n')
                                        idade = str(
                                            input('\033[36mInforme a idade do {}º comprador:'.format(contador)))
                                    else:
                                        print('\033[31mERRO: Entrada Invalida! Informe um numero!\033[m\n')
                                        idade = str(
                                            input('\033[36mInforme a idade do {}º comprador:'.format(contador)))
                                idade = int(idade)

                                # Variaveis Acumuladoras
                                soma_idade += idade  # Soma das idades
                                ing_preco_especial += 1  # Quantidade de Meias vendidas
                                vendedor_comissionado += 1  # Quantidade de Vendas de Vendedores Comissionados
                                ingressos_restantes -= 1  # Ingresso vendido
                                contador += 1  # Contador dos ingressos comissionados

                            # Não realiza a venda, caso o usuario tenha escolhido não ter preço especial
                            elif validar_ingresso_especial == '2':
                                print(f'\033[33m{'Preço Especial Indisponivel!'}')

                    # Variaveis Acumuladoras
                    cortesia_vendedor += 1

                # Não realiza a venda caso não haja comprovante
                elif comprovante in 'Nn':
                    print(f'\033[31m{'Venda Não Relizada'}')

            # Alerta caso não haja ingressos suficientes
            elif ingressos_restantes < 11:
                print(f'\033[33m{'Ingressos Insuficientes para venda comissionada!'}')

        # Cancela a Venda
        elif tipo_venda == '3':
            print(f'\n\033[31m{'Venda Não Relizada'}')
            continue

    # Encerrar Vendas e Exibir Resultados
    if vendedor == '4':
        print(f'\033[32m{' VENDAS ENCERRADAS! ':^70}')
        print('\033[36m-' * 70)
        break

# CALCULOS DOS RESULTADOS

valor_meia = valor_ingresso / 2
valor_total_inteira = inteira * valor_ingresso
valor_total_meia = meia * valor_meia
valor_total_especial = valor_especial * valor_especial
valor_total = valor_total_inteira + valor_total_meia + valor_total_especial
ingressos_emitidos = ingressos_totais - ingressos_restantes
ingressos_vendidos = ingressos_emitidos - cortesia_vendedor

# DEFINIÇÃO DO INGRESSO MAIS VENDIDO

mais_vendido = ''
if inteira == 0 and meia == 0 and ing_preco_especial == 0:
    mais_vendido = 'Nenhum ingresso vendido'
elif inteira > meia and inteira > ing_preco_especial:
    mais_vendido = 'Inteira'
elif meia > inteira and meia > ing_preco_especial:
    mais_vendido = 'Meia'
elif ing_preco_especial > inteira and ing_preco_especial > meia:
    mais_vendido = 'Preço Especial'
elif inteira == meia == ing_preco_especial:
    mais_vendido = 'Quantidade de Ingressos igual para todos os tipos'
elif inteira == meia and inteira != ing_preco_especial:
    mais_vendido = 'Inteira e Meia'
elif inteira == ing_preco_especial and inteira != meia:
    mais_vendido = 'Inteira e Preço Especial'
elif meia == ing_preco_especial:
    mais_vendido = 'Meia e Preço Especial'
elif cortesia == 0:
    mais_vendido = 'Nenhum ingresso emitido'

# EXIBIÇÃO DOS RESULTADOS
print(f'\n\033[36m{' RESULTADOS ':=^70}')

# Condição caso nenhum ingresso seja emitido
if ingressos_emitidos != 0:
    print('\033[32mQuantidade de Ingressos emtidos: {}'.format(ingressos_emitidos))
    print('Quantidade de Ingressos não emitidos: {}'.format(ingressos_restantes))
    print('Quantidade de Inteiras Vendidas: {}'.format(inteira))
    print('Quantidade de Meias-Entradas Totais: {}'.format(meia))
    print('Quantidade de Meias-Entradas Estudante: {}'.format(meia_estudante))
    print('Quantidade de Meias-Entradas Idoso: {}'.format(meia_outros))
    print('Quantidade de Ingresso Preço Especial: {}'.format(ing_preco_especial))
    print('Quantidade de Cortesias: {}'.format(cortesia))
    print('Quantidade de Cortesis dos Vendedores: {}'.format(cortesia_vendedor))
    print('Quantidade de Ingressos vendidos por vendedores comissionados: {}'.format(vendedor_comissionado))
    print('Valor Total Arrecadados: {}'.format(valor_total))
    print('Valor total de inteiras: {}'.format(valor_total_inteira))
    print('Valor total de meias: {}'.format(valor_total_meia))
    print('Valor total de ingresso com preço especial: {}'.format(valor_total_especial))
    print('Maior numero de ingressos vendidos: {}'.format(mais_vendido))

    # Condição para evitar erro de divisão por zero
    if ingressos_emitidos != 0:
        print('Media das idades dos compradores: {:.2f}'.format(soma_idade / ingressos_vendidos))
    else:
        print('Nenhum Ingresso Emitido')
else:
    print(f'{'\033[31m NENHUM INGRESSO EMITIDO ':^70}')
print('\033[36m-' * 70)

