# Programa de conversão números inteiros em diferentes bases numéricas: decimal, binário, octal e hexadecimal.

print("-Programa de Conversão de bases numéricas-")
print('Escolha uma das opções abaixo:')
print("1 - Decimal para binário")
print("2 - Decimal para octal")
print("3 - Decimal para hexadecimal")
print("4 - Binário para decimal")
print("5 - Binário para octal")
print("6 - Binário para hexadecimal")
print("7 - Octal para decimal")
print("8 - Hexadecimal para decimal")
print("9 - Hexadecimal para binário")
print("10 - Sair")

opcao = int(input("Digite a opção desejada: "))
while opcao != 10:
    if opcao == 1:
        num = int(input("Digite o número decimal: "))
        print("O número", num, "em binário é:", bin(num))
    elif opcao == 2:
        num = int(input("Digite o número decimal: "))
        print("O número", num, "em octal é:", oct(num))
    elif opcao == 3:
        num = int(input("Digite o número decimal: "))
        print("O número", num, "em hexadecimal é:", hex(num))
    elif opcao == 4:
        num = input("Digite o número binário: ")
        print("O número", num, "em decimal é:", int(num, 2))
    elif opcao == 5:
        num = input("Digite o número binário: ")
        print("O número", num, "em octal é:", oct(int(num, 2)))
    elif opcao == 6:
        num = input("Digite o número binário: ")
        print("O número", num, "em hexadecimal é:", hex(int(num, 2)))
    elif opcao == 7:
        num = input("Digite o número octal: ")
        print("O número", num, "em decimal é:", int(num, 8))
    elif opcao == 8:
        num = input("Digite o número hexadecimal: ")
        print("O número", num, "em decimal é:", int(num, 16))
    elif opcao == 9:
        num = input("Digite o número hexadecimal: ")
        print('O número', num, 'em binário é: ', bin(int(num, 16)))
    else:
        print("Opção inválida!")

    print(" \n -Reinicialização do Programa de Conversão de bases numéricas-")
    print('>Escolha uma das opções abaixo: ')
    print("1 - Decimal para binário")
    print("2 - Decimal para octal")
    print("3 - Decimal para hexadecimal")
    print("4 - Binário para decimal")
    print("5 - Binário para octal")
    print("6 - Binário para hexadecimal")
    print("7 - Octal para decimal")
    print("8 - Hexadecimal para decimal")
    print("9 - Hexadecimal para binário")
    print("10 - Sair")
    opcao = int(input("Digite a opção desejada: "))
print("Você saiu do programa: Fim do programa!")

