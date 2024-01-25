# Programa de conversão para binário ASCII

def converter_para_binario_ascii(entrada): # função que converte a entrada para binário ASCII
    return ' '.join(format(ord(i), '08b') for i in entrada) # retorna a conversão da entrada para binário ASCII

print('Digite qualquer coisa para converter em binário ASCII: ') # pede ao usuário para digitar algo
qualquer_coisa = input() # recebe a entrada do usuário
resultado = converter_para_binario_ascii(qualquer_coisa) # chama a função para converter a entrada

print('A conversão de', qualquer_coisa, 'para binário ASCII é:', resultado) # imprime o resultado da conversão

