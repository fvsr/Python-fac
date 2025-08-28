
#Abre "dados.txt" como "arquivo". 
with open('dados.txt', encoding='utf-8') as arquivo:
    #Lê o arquivo e coloca o conteúdo em "texto"
    texto = arquivo.read()
    #Conta quantas vezes a palavra "Olá" aparece.
    contador = texto.count("Olá")
    #Imprime o resultado da contagem.
    print("Total de 'Olás' é:", contador)