# utilizando esse repositorio para estudo da estrutura basica do python
# nota: Documentacao do Python https://docs.python.org/3/

# metodo
import random


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def print_soma(num1):
    print({num1} + 54)


# Press the green button in the gutter to run the script.
# nota: a main do python e uma funcao


if __name__ == '__main__':
    print_hi('PyCharm')

    # Utilizando variaveis
    # nota: Toda as variaveis sao objetos para o python
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
    print("\n")

    # Condicoes

    print("<<<<Jogo de Adivinacao!>>>>")
    print("\n")
    num_screto = random.randrange(1, 10)
    chute_str = input("Digite um numero: ")

    # convertendo str em int
    chute = int(chute_str)
    # num_range = int[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # validar numero

    if num_screto == chute:
        print("\n")
        print("Acertou!")
    else:
        print("Errou!")
    print("Fim de Jogo!")
    print("\n")

    # desafio Curso em video 1
    nome_entrada = input("Qual e seu nome? ""\n")
    print("Ola", nome_entrada, "! prazer em te conhecer !")

    # desafio Curso em video 2
    dia_nasc = input("Dia =")
    mes_nasc = input("Mes =")
    ano_nasc = input("Ano =")
    print(f"Voce nasceu no dia {dia_nasc} de {mes_nasc} de {ano_nasc}. Correto ? ")

    # desafio Curso em video 3
    num_1 = int(input("Digite o primeiro numero:"))
    num_2 = int(input("Digite o segundo numero:"))
    print(num_1+num_2)



