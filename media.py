#!/usr/bin/python3


nome = input("Informe o nome do aluno: ")
qtd = int(input('Quantas notas para calcular a média: '))

soma = 0

for i in range(qtd):
    nota = float(input("Informe a nota {0}: ".format(i+1)))
    if nota > 10 or nota < 0:
        qtd -=1
        print("Nota inválida")
        continue
    soma += nota 

media = soma / qtd
# :.2f formatação de casas decimais
print("A média do aluno {0} é: {1:.2f}".format(nome, media))