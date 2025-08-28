def zenit_polar_replace(text):
    # Aplicar a codificação ZENIT POLAR utilizando o método replace
    replacements = [('z', 'p'), ('e', 'o'), ('n', 'l'), ('i', 'a'), ('t', 'r'), #minúsculas
                    ('Z', 'P'), ('E', 'O'), ('N', 'L'), ('I', 'A'), ('T', 'R')] #maiúsculas
    for old, new in replacements: #Onde "old" é o primeiro da lista e "new" o segundo.
        text = text.replace(old, new) #Carrega uma tupla e varre a substring, 
                                      #substituindo todas as ocorrências de "old" por "new",
                                      #depois carrega a próxima dupla e recomeça,
                                      #até o fim das tuplas.
    return text
 
def main():
    # Entrada da frase e aplicação da codificação
    phrase = "The quick brown fox jumps over the lazy dog"
    phrase = phrase.title()  #primeira letra de cada palavra em maiúscula
    print("Title:",phrase)
    print("Variável 'phrase':",type(phrase))

    # Dividir a frase em palavras
    words = phrase.split() 
    print("Variável 'words':",type(words))
 
    # Processar cada palavra na lista usando ZENIT POLAR
    coded_words = [zenit_polar_replace(word) for word in words] #Lista carrega cada palara processada.
    print("Variável 'coded_words':",type(words))

    # Juntar todas as palavras codificadas em uma frase
    coded_phrase = " ".join(coded_words)
    print("Variável 'coded_phrase':",type(coded_phrase))
    print("Original:", phrase)
    print("Coded:", coded_phrase)
 
if __name__ == "__main__":
    main()