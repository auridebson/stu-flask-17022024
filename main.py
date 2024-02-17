def ln(x):
    print("-"*x)

def calcula():
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    resultado = x + y
    return resultado

ln(30)
while True:
    menu = int(input("""
        1 - Soma
        2 - Subtração
        3 - Divisão
        4 - Multiplicação
        0 - Sair
    """))
    if menu == 0:
        break
    elif menu == 1:
        res = calcula()
        ln(10)
        print(res)
        ln(10)

ln(30)
