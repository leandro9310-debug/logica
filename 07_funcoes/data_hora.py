import datetime
import calendar

meses = ["Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro"]

dias_semana = ["segunda-feira",
               "terça-feira",
               "quarta-feira",
               "quinta-feira",
               "sexta-feira",
               "sábado",
               "domingo"]

data = datetime.date(2024, 12,21)

print (data)

hoje = datetime.date.today()
print(hoje)
print(hoje.strftime("%d/%m/%Y"))
print(f"São Paulo,{dias_semana[hoje.weekday()]}, {hoje.day} de {meses[hoje.month - 1]} de {hoje.year}")

print(f"2024 é ano bissexto:{calendar.isleap(2024)}") 

print(f"É o último dia do mês? {calendar.monthrange(2026,10)[1]}")