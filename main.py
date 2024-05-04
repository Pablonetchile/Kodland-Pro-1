import discord
from discord.ext import commands
import random
from aa import token
from time import sleep

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("ja" * count_heh)

@bot.command()
async def Chiste(ctx):
    a = random.randint(0, 3)
    if a == 0:
        await ctx.send('Vas a caer @lore :rage:')
    elif a == 1:
        await ctx.send('Por lo menos mi papa fue a Estereo Bosé')
        sleep(2.5)
        await ctx.send('QUE TU PAPÁ ES EL N---O JOSE!?!?!!?!?')
    elif a == 2:
        for i in range(random.randint(1, 100)):
            sleep(1)
            await ctx.send('Ez')
    elif a == 3:
        await ctx.send('Ya ya mijo ya')
@bot.command()
async def Adios(ctx):
    await ctx.send('Adios :saluting_face:')
    print('Desconnected')
    await bot.close()

bot.run('token_aqui')
