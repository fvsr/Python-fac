#Manipulação de arquivos

#importação de uma biblioteca do sistema operacional
import os

#Abre um arquivo no mesmo diretório de arquivo.py, e se o arquivo não existir é criado um arquivo.
#Para que isso aconteça é preciso abrir no modo de escrita, por isso o parâmetro 'w'.
#Caso não seja usado o parâmetro 'w' vai acontecer um erro de arquivo não encontrado,
#caso o arquivo não exista.
#O parâmetro "encoding='utf-8'" determina uma fonte para a impressão.
arquivo1 = open("dados1.txt",'w', encoding='utf-8')

#A resposta para caminho absoluto do arquivo será: (/bin/python3) /workspaces/Python-fac/dados1.txt
print(os.path.abspath(arquivo1.name)) 

#imprime o texto no arquivo externo
arquivo1.write("Olá mundo!")

#A resposta para caminho relativo do arquivo será "dados1.txt",
#o que significa que o arquivo está no mesmo diretório que o código.
print(os.path.relpath(arquivo1.name))

#A saída será: <_io.TextIOWrapper name='dados1.txt' mode='w' encoding='utf-8'>
#que sáo os parâmetros de escrita em arquivo1.
print(arquivo1)