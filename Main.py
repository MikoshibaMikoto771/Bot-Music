import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix='?', intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)



client.run ("OTEyODg1NTM4ODI5MjU0Njc2.YZ2c6Q.0s-t-YIqAdTY5oPh4a-KjveTlp0")
