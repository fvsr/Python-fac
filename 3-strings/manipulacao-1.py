#Manipulação de strings

arquivo = open('dados.txt','r',encoding='utf-8')

conteudo = arquivo.read()

print("Tipo de conteúdo:", type(conteudo)) #Retorna <class 'str'>

print("Conteudo retornado pelo read:")

print(repr(conteudo)) #Retorna 'Olá, mundo!\n\nOlá, EAD.\n\nOlá, aluno!'

arquivo.close()