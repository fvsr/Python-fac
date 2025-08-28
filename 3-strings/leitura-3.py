#Manipulação de strings

arquivo = open('dados.txt','r',encoding='utf-8')

conteudo = arquivo.readlines() #Lê linha por linha e armazena numa lista

print("Tipo de conteúdo:", type(conteudo)) #Retorna <class 'list'>

print("Conteudo retornado pelo read:")

print(repr(conteudo)) #Retorna 'Olá, mundo!\n\nOlá, EAD.\n\nOlá, aluno!'

arquivo.close()