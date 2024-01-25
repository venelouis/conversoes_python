# Programa de conversão para binário

def converter_para_binario(entrada): # função que converte a entrada para binário
    try: 
        # tenta converter a entrada para um inteiro
        entrada = int(entrada) # se a entrada for um número, converte para inteiro
        return bin(entrada) # retorna a conversão da entrada para binário
    except ValueError: 
        # se a entrada não for um número, assume que é uma string
        return ' '.join(format(ord(i), 'b') for i in entrada) # retorna a conversão da entrada para binário

print('Digite qualquer coisa para converter em binário: ') # pede ao usuário para digitar algo
qualquer_coisa = input() # recebe a entrada do usuário
resultado = converter_para_binario(qualquer_coisa) # chama a função para converter a entrada

print('A conversão de', qualquer_coisa, 'para binário é:', resultado) # imprime o resultado da conversão

# Programa de conversão para binário