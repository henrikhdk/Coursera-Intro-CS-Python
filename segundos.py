segundosConverter = int(input('Por favor, entre com o número de segundos que deseja converter: '))

sec_value = segundosConverter % (24 * 3600)
horas = sec_value // 3600
dias = segundosConverter // 86400
segs_restantes = segundosConverter % 3600
minutos = segs_restantes // 60
segs_restantes_finais = segs_restantes % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segs_restantes_finais, "segundos")