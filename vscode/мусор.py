# -*- coding: utf-8 -*- 

import discord
from discord.ext import commands


prefix = ["Бот ", "Bot "]
intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix=prefix, intents=intents)

#####################################################################################
# CLIENT.EVENT - СОБЫТИЯ                                                            #
#####################################################################################
@client.event
async def on_ready():
    """БЛОК ИНСТРУКЦИЙ ВЫПОЛНЯЕМЫЙ ПО ГОТОВНОСТИ БОТА"""
    print(f"ID     : {client.user.id}\nNAME   : {client.user.name}\nSTATUS : ONLINE")

@client.event
async def on_member_join(member):
    """БЛОК ИНСТРУКЦИЙ ЕСЛИ ПОЛЬЗОВАТЕЛЬ ПРИСОЕДИНЯЕТСЯ К СЕРВЕРУ"""
    print(f"Пользователь {member} вошел на сервер.")

@client.event
async def on_member_remove(member):
    """БЛОК ИНСТРУКЦИЙ ЕСЛИ ПОЛЬЗОВАТЕЛЬ ПОКИДАЕТ СЕРВЕР"""
    print(f"Пользователь {member} покинул сервер.")

#@client.event
#async def on_message(message):
    """ВАРИАНТ ОТРАБОТКИ КОМАНД 01"""
    """КОГДА ИСПОЛЬЗУЕТСЯ ON_MESSAGE БОТ НАХОДИТСЯ В ПОСТОЯННОМ ОЖИДАНИИ СООБЩЕНИЙ И КОМАНДЫ КЛАССА CLIENT.COMMAND НЕ ВЫПОЛНЯЮТСЯ."""
    #if message.content == "Всем привет!":
        #await message.channel.send("Привет!")
    #else:
        #pass

#####################################################################################
# CLIENT.COMMAND - КОМАНДЫ                                                          #
#####################################################################################
@client.command(aliases = ["привет", "привет!"])
async def hello(ctx):
    """ВАРИАНТ ОТРАБОТКИ КОМАНД 02"""
    await ctx.send(f"Привет {ctx.author.mention}!")


client.run("OTcxODM4Mjc5MTM5ODU2NDQ1.YnQU7Q.tCYPbj8zt2FulX56A0BLZCST2Zs")
