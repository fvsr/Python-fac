#Formatação de strings

#Formatar strings não é mudar a fonte ou o tamanho,
#mas sim alterar texto em tempo de execução.
#Podemos usar o método "format()" ou as f-strings

#Exemplo do uso do método "format":

nome = "Maria"
idade = 30
mensagem = "Olá, {}. Você tem {} anos.".format(nome,idade)
print(mensagem)