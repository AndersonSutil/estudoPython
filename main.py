# utilizando esse repositorio para estudo da estrutura basica do python
#

# metodo
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def print_soma(num1):
    print({num1} + 54)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
# Utilizando variaveis
# nota: As variaveis sao dinamicas, mudam dependendo do valor armazenado
# nota: O python utiliza por padrao a coversao Snake_Case para os nomes de variaveis ou identificadores
# Ex: frase_inicial
    frase_inicial = 'A primeira luz que vi foi no dia:'
    dia = 15
    mes = 0o3
    ano = 1998
    print(frase_inicial, dia, mes, ano, sep="/", end="!\n")

    print(type(frase_inicial))
    print(type(dia))
    print("\n")

# Exemplo da  variavel dinamica
# nota: uma variavel dinamica so passa a existir quando atribuimos um valor a ela.

    print("<<Exemplo de variavel dinamica>>""\n")

    print(dia)
    print(type(dia))
    dia = 'Amarzenando uma string'
    print(dia)
    print(type(dia))
