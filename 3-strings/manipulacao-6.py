#Coloca uma string numa variável.
frase1 = "Eu amo comer amoras no café da manhã."

#Divide a string em uma lista de palavras usando a função "split()"
#e coloca o resultado em uma variável.
lista_termos1 = frase1.split() #
#Imprime a lista.
print(lista_termos1)

frase2 = "Amora abacaxi       abacate               banana"
lista_termos2 = frase2.split()
print(lista_termos2)

frase3 = "Carro, moto,avião"
lista_termos3 = frase3.split(',') #Determina um separador como argumento para a função "split()".
print(lista_termos3)

exit()