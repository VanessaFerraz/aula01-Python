#!/usr/bin/python3

#comentário de uma linha
'''
comentário de bloco
'''

# print ("Hello World")
# #quebra de linha de "\n"
# print("\nQuebra de linha")
# nome = input("Digite o nome: ")
# idade = input("Digite a idade: ")

# #concatenar string com variável
# print("Seu nome é {0} e sua idade é {1}".format(nome,idade))

# #conversão de valores int, float, str (cast)
# idade = int(idade)

# if (idade >= 18): 
#     print ('maior de idade')
# else:
#     print ('menor de idade')    

# num = 2
# i = 1
# print ("Tabuada com while")
# while (i <= 10):
#     tab = num * i
#     print ("{0} x {1} = {2}".format(num, i, tab))
#     i += 1
# print ("\nTabuada com for")
# for x in range(1, 10, 1):
#     tab = num * x
#     print ("{0} x {1} = {2}".format(num, x, tab))

fruta = ["Laranja", "Abacaxi", "Uva" ] 
#A função enumerate permite pegar o índice e o valor de uma lista
for num,item in enumerate(fruta): 
    print ("{} esta na posicao {}".format(item,num))
