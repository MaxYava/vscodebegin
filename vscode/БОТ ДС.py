import discord
from discord.ext import commands

config = {
    'token': 'your-token',
    'prefix': 'prefix',
}

bot = commands.Bot(command_prefix=config['prefix'])

@bot.event
async def on_message(ctx):
    if ctx.author != bot.user:
        await ctx.reply(ctx.content)

bot.run(config['OTcxODM4Mjc5MTM5ODU2NDQ1.GJDrL1.8j0-nll-qSLh-2KmBtd3OWn98vV0yFyZUAMnh8'])
