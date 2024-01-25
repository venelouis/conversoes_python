# Funções para conversão de grandezas elétricas:
# Ampere, Herzt, Volt e Watt.

print("Programa de conversão de grandezas elétricas")
print("Escolha uma das opções abaixo:")
print("1 - Ampere para Hertz")
print("2 - Ampere para Volt")
print("3 - Ampere para Watt")
print("4 - Hertz para Ampere")
print("5 - Hertz para Volt")
print("6 - Hertz para Watt")
print("7 - Volt para Ampere")
print("8 - Volt para Hertz")
print("9 - Volt para Watt")
print("10 - Watt para Ampere")
print("11 - Watt para Hertz")
print("12 - Watt para Volt")
print("13 - Sair")

opcao = int(input("Digite a opção desejada: "))
while opcao != 13:
    if opcao == 1:
        num = float(input("Digite o valor em Ampere: "))
        print("O valor", num, "em Hertz é:", num / 2)
    elif opcao == 2:
        num = float(input("Digite o valor em Ampere: "))
        print("O valor", num, "em Volt é:", num * 2)
    elif opcao == 3:
        num = float(input("Digite o valor em Ampere: "))
        print("O valor", num, "em Watt é:", num * 2)
    elif opcao == 4:
        num = float(input("Digite o valor em Hertz: "))
        print("O valor", num, "em Ampere é:", num * 2)
    elif opcao == 5:
        num = float(input("Digite o valor em Hertz: "))
        print("O valor", num, "em Volt é:", num * 2)
    elif opcao == 6:
        num = float(input("Digite o valor em Hertz: "))
        print("O valor", num, "em Watt é:", num * 2)
    elif opcao == 7:
        num = float(input("Digite o valor em Volt: "))
        print("O valor", num, "em Ampere é:", num / 2)
    elif opcao == 8:
        num = float(input("Digite o valor em Volt: "))
        print("O valor", num, "em Hertz é:", num / 2)
    elif opcao == 9:
        num = float(input("Digite o valor em Volt: "))
        print("O valor", num, "em Watt é:", num / 2)
    elif opcao == 10:
        num = float(input("Digite o valor em Watt: "))
        print("O valor", num, "em Ampere é:", num / 2)
    elif opcao == 11:
        num = float(input("Digite o valor em Watt: "))
        print("O valor", num, "em Hertz é:", num / 2)
    elif opcao == 12:
        num = float(input("Digite o valor em Watt: "))
        print("O valor", num, "em Volt é:", num / 2)
    else:
        print("Opção inválida!")

print("Fim do programa")