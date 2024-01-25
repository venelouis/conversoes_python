# Programa de conversão de grandezas computacionais

def converter_grandezas_computacionais(quantidade, unidade_origem, unidade_destino): # função que converte grandezas computacionais
    grandezas = { # dicionário com as grandezas computacionais e seus valores em bytes
        'Byte': 1,
        'Kilobyte (KB)': 1024,
        'Megabyte (MB)': 1024**2,
        'Gigabyte (GB)': 1024**3,
        'Terabyte (TB)': 1024**4,
    }

    bytes = quantidade * grandezas[unidade_origem] # converte a quantidade para bytes
    resultado = bytes / grandezas[unidade_destino] # converte os bytes para a unidade de destino

    print(f'{quantidade} {unidade_origem} equivale a {resultado:.2f} {unidade_destino}') # imprime o resultado da conversão

opcoes = {
    '1': ('Byte', 'Kilobyte (KB)'),
    '2': ('Byte', 'Megabyte (MB)'),
    '3': ('Byte', 'Gigabyte (GB)'),
    '4': ('Byte', 'Terabyte (TB)'),
    '5': ('Kilobyte (KB)', 'Megabyte (MB)'),
    '6': ('Kilobyte (KB)', 'Gigabyte (GB)'),
    '7': ('Kilobyte (KB)', 'Terabyte (TB)'),
    '8': ('Megabyte (MB)', 'Gigabyte (GB)'),
    '9': ('Megabyte (MB)', 'Terabyte (TB)'),
    '10': ('Gigabyte (GB)', 'Terabyte (TB)'),
    '11': ('Kilobyte (KB)', 'Byte'),
    '12': ('Megabyte (MB)', 'Byte'),
    '13': ('Gigabyte (GB)', 'Byte'),
    '14': ('Megabyte (MB)', 'Kilobyte (KB)'),
    '15': ('Gigabyte (GB)', 'Kilobyte (KB)'),
    '16': ('Terabyte (TB)', 'Kilobyte (KB)'),
    '17': ('Gigabyte (GB)', 'Megabyte (MB)'),
    '18': ('Terabyte (TB)', 'Megabyte (MB)'),
    '19': ('Terabyte (TB)', 'Gigabyte (GB)'),
    # adicione mais opções conforme necessário
}

print('Escolha entre as opções abaixo:')
for opcao, unidades in opcoes.items(): # itera sobre as opções e unidades
    print(f'{opcao}- {unidades[0]} para {unidades[1]}') # imprime as opções e unidades

escolha = input('Digite o número da opção escolhida: ') # pede ao usuário para escolher uma opção
unidade_origem, unidade_destino = opcoes[escolha] # pega as unidades de origem e destino da opção escolhida

quantidade = float(input(f'Digite a quantidade de {unidade_origem} a ser convertida: ')) # pede ao usuário para digitar a quantidade a ser convertida
converter_grandezas_computacionais(quantidade, unidade_origem, unidade_destino) # chama a função para converter as grandezas computacionais
# Path: conversao_grandezas_computacionais.py
# Compare this snippet from conversao_binaria_ASCII.py:
# # Programa de conversão para binário ASCII