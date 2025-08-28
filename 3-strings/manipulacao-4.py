
with open('dados.txt', encoding='utf-8') as arquivo:
    contador = 0
    print('Representação do arquivo')
    for linha in arquivo:  #Para cada linha no arquivo,
        print(repr(linha)) #escreva a representação da linha,
        if linha:          #se existir uma linha,
            contador += 1  #acrescentar a contagem total.
    print("Total de linhas:", contador) #Imprimir o número de linhas, no caso 5 linhas.

with open('dados.txt', encoding='utf-8') as arquivo:
    contador = 0
    print("Representação do arquivo após a função strip():")
    for linha in arquivo:  #Para cada linha no arquivo,
        linha_limpa = linha.strip() #retira as quebras de linha
        print(repr(linha_limpa)) #escreva a representação da linha,
        if linha_limpa:          #se existir uma linha,
            contador += 1        #acrescentar a contagem total.
    print("Total de linhas:", contador) #Imprimir o número de linhas, no caso 3 linhas, 
                                        #porque o strip eliminou duas linhas.