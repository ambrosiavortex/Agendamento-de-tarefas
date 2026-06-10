print ("Agendamento de exames.")

dias = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira"]
horarios = ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"]
exames_agendados = [] #Dicionário para armazenar os exames agendados

#Função de menu para o usuário
def menu():
    print ("1. Agendar exame")
    print ("2. Listar exames")
    print ("3. Cancelar exame")
    print ("4. Sair")
    opcao = input ("Escolha uma opção: ")
    return opcao

#Função para agendar exame
def agendar_exame():  
    print ("Agendamento de exame")

    paciente = input ("Digite o nome do paciente:")

    dia = input ("Escolha o dia (Dias utéis ): ")
    if dia not in dias:
        print ("Dia inválido. Tente novamente.")
        return
    
    horario = input ("Escolha o horário (08:00, 09:00, 10:00, 11:00, 12:00, 13:00, 14:00, 15:00, 16:00, 17:00): ")
    if horario not in horarios:
        print ("Horário inválido. Tente novamente.")
        return
    
    exame = {"dia": dia, "horario": horario, "paciente": paciente}
    if exame in exames_agendados:
        print ("Exame já agendado para esse dia e horário. Tente novamente.")
        return
    exames_agendados.append(exame)
    print ("Exame agendado com sucesso.") 

while True:
    opcao = menu()

    match opcao:
        case 1:
            agendar_exame()

     