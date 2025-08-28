#Formatação de datas

from datetime import datetime
hoje = datetime.now()

#Método "format()":
#A desvantagem do método "format()" é que é necessário outro método para finalizar a formatação.
data_formatada = hoje.strftime("Data: %d/%m/%Y") 

print(data_formatada)

#Usando F-string:

data_formatada = f"Data: {hoje:%d/%m/%y}"

print(data_formatada)