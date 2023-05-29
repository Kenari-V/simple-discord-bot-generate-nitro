import random
import discord
from discord.ext import commands
from discord.commands import Option
from settingtoken import token


bot = discord.Bot()

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="test"))
    print('Login {0.user}'.format(bot))

huruf_besar = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
huruf_kecil = 'abcdefghijklmnopqrstuvwxyz'
nomber = '0123456789'

@bot.slash_command(name="generate", description="generate nitro discord")
async def generatediscord(ctx):
    besar, kecil, number, = True, True , True
    all = ""

    if besar:
        all += huruf_besar
    if kecil:
        all += huruf_kecil
    if number:
        all += nomber

        length = 16

        nitrogen = ''.join(random.sample(all, length))

    await ctx.respond('discord.gift/'+nitrogen)           



bot.run(token)
