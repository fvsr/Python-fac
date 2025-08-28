#O programa converte o texto escrito para maiúsculas.

#função principal
def main():
    #imprime uma mensagem para o usuário
    print("Digite suas frases. Digite 'sair' para terminar e salvar o arquivo.")
    #cria uma lista que vai receber as frases que o usuário digitar
    frases = []

    #laço contínuo para capturar as entradas do usuário
    while True:
        #captura o teclado por meio da função input, a seta, ">" sugere o início do texto
        entrada = input("> ")
        #para sair do laço digitar "sair"
        if entrada.lower() == "sair": #Para sair escrever "sair" isoladamente e dar "Enter".
            break
        #cada frase capturada é somada ao arquivo
        frases.append(entrada)

    #Abre um arquivo no modo de escrita.
    with open("meu_arquivo.txt","w") as arquivo:
        #Para cada frase no modo de entrada, salva no arquivo com uma quebra de linha.
        for frase in frases:
            arquivo.write(frase + "\n")
    

    print("Arquivo original criado. Agora vamos manipular os dados.")
    #Cria uma lista, "[]", para receber os dados originais capturados inicialmente.
    dados_modificados = []
    #Abre o arquivo original no modo leitura.
    with open("meu_arquivo.txt", "r") as arquivo: #A palavra "arquivo" está dentro do escopo do "with"
        for linha in arquivo:
            dados_modificados.append(linha.strip().upper()) #Retira os espaços, coloca em maiúscula e salva na lista.

    #Sobrescreve os dados originais com os dados modificados.
    with open("meu_arquivo.txt", "w") as arquivo:
        for linha in dados_modificados:
            arquivo.write(linha + "\n")
    print("O arquivo foi sobrescrito com os dados modificados.")

if __name__ == "__main__":
    main()