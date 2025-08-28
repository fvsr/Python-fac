frase = "Eu amo comer amoras no café da manhã."

#Resultado obtido usando o método "count()" diretamente.
print("Contagem direta: ", frase.count('amo')) #Retorna 2.

#Resultado obtido utilizando a quebra da frase em palvras.
contador = 0
lista_termos = frase.split()
for termo in lista_termos:
    if termo == 'amo':
        contador += 1
print("Contagem correta:", contador) #Retorna 1.