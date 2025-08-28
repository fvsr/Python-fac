arquivo = open('dados.txt','r',encoding='utf-8')

conteudo = arquivo.readline() #Lê uma linha do arquivo.

print("Tipo de conteúdo: ", type(conteudo)) #Retorna  <class 'str'>

print("Conteúdo retornado pelo read:") #Retorna 'Olá, mundo!\n'

print(repr(conteudo)) #Retorna a representação canónica de um objeto.

proximo_conteudo = arquivo.readline() #Lê a linha seguinte do arquivo.
print("Próximo conteúdo retornado: ") #Retorna '\n', porque a próxima linha no arquivo é quebra de linha.
print(repr(proximo_conteudo))

proximo_conteudo = arquivo.readline() #Lê a linha seguinte do arquivo, pode continuar indefinidamente.
print("Próximo conteúdo retornado: ") #Retorna '\n', porque a próxima linha no arquivo é quebra de linha.
print(repr(proximo_conteudo))

arquivo.close()