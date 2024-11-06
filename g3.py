from datetime import datetime

def mostrar_data_hora():
    agora =  datetime.datetime.now #REMOVA O 0 E COMPLETE A VARIÁVEL PARA RETORNAR A DATA E HORA ATUAL
    print("Data e Hora atuais:")
    print(agora)
    print("Formato: DD/MM/AAAA HH:MM:SS")
    print(agora.strftime("%d/%m/%Y %H:%M:%S"))

mostrar_data_hora()
