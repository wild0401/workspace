import discord
from discord.ext import commands

bot = commands.Bot(command_preFix='[')
bot.run('')
@bot.event
async def om_ready():
    print("123")
