#Atributos de arquivos

#Atributo "name"
#print(arquivo.name) #O atributo "name" retorna o nome do arquivo associado ao objeto "arquivo".

#Atributo "mode"
#print(arquivo.mode) #O atributo "mode" retorna o modo em que o atributo foi aberto,
#como leitura 'r', escrita 'w', adição 'a', etc.
#O modo adição abre um arquivo para escrita, mas não sobrescreve o que já foi escrito
#anteriormente no arquivo, apenas adiciona linhas abaixo da última linha que já existe.

#Atributo "closed"
"""
print(arquivo.closed)
arquivo.close()
print(arquivo.closed)
"""
#O atributo "closed" verifica se o arquivo está fechado,
#retorna "true" se estiver fechado e "false" caso contrário.

#Caminho do arquivo
"""
import os

print(os.path.relpath('exemplo.txt'))
print(os.path.abspath('exemplo.txt'))
"""
#Acessados por meio do módulo "os".
#O comando "path" é um submódulo de "os".
#O comando "relpath" retorna o caminho relativo do arquivo, em relação ao diretório atual.
#O comando "abspath" retorna o caminho absoluto do arquivo no sistema de arquivos.

"""
"Talk is cheap, show me the code." Linus Torvalds, criador do Linux.
"""

#Exemplo de código
import os

#Abre um arquivo no modo escrita.
arquivo = open('exemplo.txt', 'w', encoding='utf-8')

#Exibe os atributos do arquivo.
print("Nome do arquivo: ", arquivo.name)
print("Modo de abertura: ", arquivo.mode)
print("O arquivo está fechado? ", arquivo.closed)

#Escrevendo no arquivo
arquivo.write("Olá mundo!")

#Fechando o arquivo
arquivo.close()

#Verificando se o arquivo está fechado.
print("O arquivo está fechado agora?", arquivo.closed)

#Exibindo caminhos relativo e absoluto
relpath = os.path.relpath('exemplo.txt')
abspath = os.path.abspath('exemplo.txt')

print("Caminho relativo:", relpath)
print("Caminho absoluto:", abspath)

#Saída:
"""
Nome do arquivo:  exemplo.txt
Modo de abertura:  w
O arquivo está fechado?  False
O arquivo está fechado agora? True
Caminho relativo: exemplo.txt
Caminho absoluto: /workspaces/Python-fac/exemplo.txt
"""