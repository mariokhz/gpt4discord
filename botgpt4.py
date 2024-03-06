import os
import sys
from embedsplit import emsplit
from textsplit import txtsplit
import gpt4 as g
import discord
import random
import time
from discord.utils import get
from discord_easy_commands import EasyBot
intents = discord.Intents.all()
bot = EasyBot(intents = intents)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    print("Mensaje anterior enviado por: " + message.author.name)
    respuesta = g.generar(message.author.name + ':' + message.content)
    embeds = emsplit(respuesta)
    txtlist = txtsplit(respuesta, embeds)

    for i in range(0, len(txtlist)):
        await message.channel.send(txtlist[i])

def main(system, modelo, dtoken, openaitoken):
    g.setsystem(system, modelo)
    g.setopenai(openaitoken)
    bot.run(dtoken)
