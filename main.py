print ("Agendamento de exames.")

dias = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira"]
horarios = ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"]
exames_agendados = [] #Lista para armazenar os exames agendados

exames_agendados.append({"id": 1, "dia": "Segunda-feira", "horario": "08:00", "paciente": "Light Yagami"})

#Função de menu para o usuário
def menu():
    print ("1. Agendar exame")
    print ("2. Cancelar exame")
    print ("3. Listar exames")
    print ("4. Sair")
    opcao = input ("Escolha uma opção: ")
    return opcao

#Função para agendar exame
def agendar_exame():  
    id = 0 #Variável para ids
    print ("Agendamento de exame")

    paciente = input ("Digite o nome do paciente: ")

    dia = input ("Escolha o dia (Dias úteis ): ")
    if dia not in dias:
        print ("Dia inválido. Tente novamente.")
        return
    
    horario = input ("Escolha o horário (08:00, 09:00, 10:00, 11:00, 12:00, 13:00, 14:00, 15:00, 16:00, 17:00): ")
    if horario not in horarios:
        print ("Horário inválido. Tente novamente.")
        return
    
    id += 1 

    exame = {"id": id, "dia": dia, "horario": horario, "paciente": paciente}
    if exame in exames_agendados:
        print ("Exame já agendado para esse dia e horário. Tente novamente.")
        return
    exames_agendados.append(exame)

    print (f"Exame agendado com sucesso.{exame}")

#Função para cancelar exame
def cancelar_exame():
    print ("Cancelamento de exames.")

    id_exame = input ("Digite o id do exame cancelável: ")

    for exame in exames_agendados:
        if id_exame == exame["id"]:
            exames_agendados.remove(exame)

    print ("Exame cancelado com sucesso!")

def listar_exames():
    print ("Exames já agendados: ")

    if len(dias) == 0:
        print ("Não há exames agendados.")
    else:
        print (exames_agendados)
        

#Loop do menu
while True:
    opcao = menu()

    match opcao:
        case "1":
            agendar_exame()
        case "2":
            cancelar_exame()
        case "3":
            listar_exames()
        case "4":
            break