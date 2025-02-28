inicio = input().split()
horario = input().split()
segundos_que_iniciou = int(horario[0]) * 3600 + int(horario[2]) * 60 + int(horario[4])
em_segundosinicio = 86400 - segundos_que_iniciou

fim = input().split()
horario2 = input().split()
dias_passados = int(fim[1]) - int(inicio[1])
horas_passadas = (dias_passados - 1) * 24
horas_passadas_em_segundos = horas_passadas * 3600
em_segundosfim = int(horario2[0]) * 3600 + int(horario2[2]) * 60 + int(horario2[4])

segundos_totais = horas_passadas_em_segundos + em_segundosfim + em_segundosinicio

horas_maximas = segundos_totais // 3600
dias = horas_maximas // 24
horas = horas_maximas % 24
resto0_segundos = segundos_totais % 3600
minutos = resto0_segundos // 60
segundos = resto0_segundos % 60

print(f'{dias} dia(s)\n{horas} hora(s)\n{minutos} minuto(s)\n{segundos} segundo(s)')
