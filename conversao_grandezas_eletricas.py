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


'''
As grandezas elétricas podem ser divididas em dois grupos: grandezas básicas e grandezas derivadas.

Grandezas básicas são aquelas que não podem ser definidas em termos de outras grandezas. As quatro grandezas elétricas básicas são:

- Tensão elétrica (V): É a força que impulsiona os elétrons através de um circuito elétrico. É medida em volts (V).
- Corrente elétrica (A): É a quantidade de elétrons que passam por um ponto de um circuito elétrico em um determinado período de tempo. É medida em amperes (A).
- Resistência elétrica (Ω): É a oposição que um material oferece à passagem da corrente elétrica. É medida em ohms (Ω).
- Potência elétrica (W): É a quantidade de energia elétrica que é transformada, usada ou dissipada em um determinado período de tempo. É medida em watts (W).

Grandezas derivadas são aquelas que podem ser definidas em termos de grandezas básicas. 
Algumas grandezas elétricas derivadas são:

Capacitância elétrica (C): É a capacidade de um material armazenar energia elétrica. É medida em farads (F).
Indutância elétrica (L): É a capacidade de um material armazenar energia magnética. É medida em henrys (H).
Frequência elétrica (f): É o número de ciclos de uma onda elétrica em um determinado período de tempo. É medida em hertz (Hz).
Impedância elétrica (Z): É a oposição total que um circuito elétrico oferece à passagem da corrente elétrica. É medida em ohms (Ω).
Coeficiente de temperatura da resistência elétrica (α): É a variação da resistência elétrica de um material em função da temperatura. É medido em ohms por grau Celsius (Ω/°C).
Coeficiente de temperatura da capacitância elétrica (β): É a variação da capacitância elétrica de um capacitor em função da temperatura. É medido em farads por grau Celsius (F/°C).
Coeficiente de temperatura da indutância elétrica (γ): É a variação da indutância elétrica de uma bobina em função da temperatura. É medido em henrys por grau Celsius (H/°C).

Outras grandezas elétricas derivadas incluem:

Fator de potência (FP): É a relação entre a potência ativa e a potência aparente de um circuito elétrico. É um número entre 0 e 1.
Energia elétrica (E): É a quantidade de trabalho que pode ser realizado por uma corrente elétrica. É medida em joules (J).
Potência aparente (S): É a potência total de um circuito elétrico, que é a soma da potência ativa e da potência reativa. É medida em volt-amperes (VA).
Potência reativa (Q): É a parte da potência aparente de um circuito elétrico que não é convertida em energia. É medida em volt-amperes reativos (VAR).
Eficiência elétrica (η): É a relação entre a potência ativa e a potência total de um circuito elétrico. É um número entre 0 e 1.
As grandezas elétricas são importantes para o estudo e a compreensão da eletricidade. Elas são usadas para descrever e medir os fenômenos elétricos, e são essenciais para o desenvolvimento de dispositivos e sistemas elétricos.

Essas são todas as grandezas elétricas básicas e derivadas reconhecidas pelo Sistema Internacional de Unidades (SI). 
No entanto, existem outras grandezas elétricas que são usadas em áreas específicas da eletricidade, como a eletrônica, a telecomunicações e a engenharia elétrica. Por exemplo, na eletrônica, são usadas grandezas como a impedância complexa, que é uma combinação da impedância elétrica e da reatância elétrica.

Além disso, existem grandezas elétricas que são derivadas de outras grandezas elétricas, como a energia elétrica, que é derivada da potência elétrica.

Em resumo, as grandezas elétricas são essenciais para o estudo e a compreensão da eletricidade. 
Elas são usadas para descrever e medir os fenômenos elétricos, e são essenciais para o desenvolvimento de dispositivos e sistemas elétricos.
'''
