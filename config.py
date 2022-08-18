import datetime
import nextcord
from nextcord.ext import commands

def current_date_format(date):
    months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = date.day
    month = months[date.month - 1]
    year = date.year
    hour = date.hour
    minute = date.minute
    second = date.second
    messsage = "{} {}, {}, {}:{}:{}".format(month, day, year, hour, minute, second)

    return messsage

ServersID = 994288503103959051
Fecha_actual = current_date_format(datetime.datetime.now())
#Fecha_procesada = Fecha_actual.__format__('%d/%m/%Y, %H:%M:%S')

intents = nextcord.Intents.default()
intents.members = True
#intents.message_content = True
bot = commands.Bot(command_prefix='-', intents=intents, help_command=None, case_insensitive=True)