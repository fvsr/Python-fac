#O programa converte o texto digitado para maiúsculas.
#Este programa interage com o arquivo de texto "meu_arquivo.txt", que está no mesmo diretório.

#função principal
def main():
    #Imprime uma mensagem para o usuário com instruções sobre como usar o programa.
    print("Digite suas frases. Digite 'sair' para terminar e salvar o arquivo.")
    #Cria uma lista vazia que vai armazenar as frases que o usuário digitar.
    frases = []

    #Laço contínuo para capturar as entradas do usuário.
    while True:
        #Captura o teclado por meio da função input, a seta, ">", sugere o início do texto.
        #A digitação do usuário é armazenada na variável entrada, após cada comando "Enter".
        entrada = input("> ") #A variável "entrada" é tipo string.
        #Para sair do laço digitar "sair", case insensitive.
        if entrada.lower() == "sair": #Para sair escrever "sair" isoladamente e dar "Enter".
            break
        #Se não foi "sair", adiciona frase capturada à lista de frases, na lista "frases".
        frases.append(entrada)

    #Abre um arquivo no modo de escrita.
    #O comando "with" garante que o arquivo será fechado automaticamente.
    #O comando "encoding='utf-8'" evita problemas com acentos no Windows, mas o Codespace é Linux.
    #O camando "with" faz com que o arquivo seja fechado automaticamente.
    with open("meu_arquivo.txt","w",encoding='utf-8') as arquivo:  
        #Para cada frase coletada na lista, escreve no arquivo com uma quebra de linha.
        for frase in frases:
            arquivo.write(frase + "\n")

    print("Arquivo original criado. Agora vamos manipular os dados.")
    #Cria uma outra lista, "[]", para receber os dados originais capturados inicialmente.
    dados_modificados = []
    #Abre o arquivo original no modo leitura.
    with open("meu_arquivo.txt", "r") as arquivo: #A palavra "arquivo" está dentro do escopo do "with"
        for linha in arquivo:
            dados_modificados.append(linha.strip().upper()) #Retira os espaços em branco e quebras de linha, 
                                                            #converte para maiúscula e salva na lista
                                                            #"dados_modificados".

    #Sobrescreve os dados originais com os dados modificados,
    #adicionando uma quebra de linha a cada frase.
    with open("meu_arquivo.txt", "w") as arquivo:
        for linha in dados_modificados:
            arquivo.write(linha + "\n")
    print("O arquivo foi sobrescrito com os dados modificados.")

if __name__ == "__main__": #Verifica se o script está sendo executado diretamente,
                           #não importado como módulo.
    main() #Chama afunção main.