#!/usr/bin/python3

#criando uma lista sem elementos
lista = []
lista2 = []

#laço para inserir as letras do alfabeto segundo os valores da tabela ASC
for i in range(97,123,1):
    #insere na lista os elementos convertidos para string 
    #funcao chr recebe o numero da tabela ASC e devolve o caracter
    #funcao ord recebe o caracter da tabela ASC e devolve o seu numero
    lista.append(str(chr(i)))

#Aqui já adiciona o elemento na lista por meio do for em uma úncia linha
#list compilation mais rápido que o laço tradicional
lista2 = [chr(i) for i in range(97, 97+26)]

#if ternário
'certo' if True == True else 'errado'

#exibe toda a lista
print("{}".format(lista[:]))
print(lista)
print(lista2)

